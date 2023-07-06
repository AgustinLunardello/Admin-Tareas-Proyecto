from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse 
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from adminDB.adminDB import AdminDB
from models.userModel import *
from models.tasksModel import taskModel
from settings.settings import Settings

admin = AdminDB()
app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.post('/register-user')
async def register(user: UserModelRegister):
    try:
        admin.registerUser(user)
        return {'message': 'Successfully registered user'}
    except HTTPException as e:
        raise e
        

@app.post('/login')
async def login(user: UserModelLogin, Authorize: AuthJWT = Depends()):
    
    login = admin.loginUser(user)
    
    if login:
        token = Authorize.create_access_token(subject=user.username)
        return {'message': 'Login successful','access_token': token}
    raise HTTPException(status_code=401, detail='bad username or password')
    
@app.post('/task')
async def addTask(task: taskModel, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    try:
        id = admin.addTask(task)
        return {'message': f'Succesfull task added with id {id}'}
    except HTTPException as e:
        raise e

@app.get('/tasks/{author}')
async def getTasks(author: str, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    try:
        tasks = admin.get_all_tasks(author)
        if tasks:
            return tasks
        raise HTTPException(status_code=404, detail='Tasks not found or not exists.')
    except HTTPException as e:
        raise e

@app.get('/task/{id}/{author}')
async def getTaskByID(id: int, author: str, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    try:
        task = admin.get_task_by_id(id, author)
        if task:
            return task
        raise HTTPException(status_code=404, detail='Task not found or not exists.')
    except HTTPException as e:
        raise e

@app.delete('/task_delete/{id}/{author}')
async def deleteTask(id: int, author: str, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    try:
        responses = admin.delete_task_by_id(id, author)
        if responses:
            return {'message': 'Task delete successfully'}
        raise HTTPException(status_code=404, detail='Task not found or not exists')
    except HTTPException as e:
        raise e

@app.put('/task_new_state/{id}/{author}/{new_state}')
async def updateTask(id: int, author: str, new_state: str, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    try:
        responses = admin.update_state_task(id, author, new_state)
        if responses:
            return {'message': 'Task updated successfully'}
        raise HTTPException(status_code=404, detail='Task not found or not exists')
    except HTTPException as e:
        raise e


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)