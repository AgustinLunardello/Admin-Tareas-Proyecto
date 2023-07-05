from fastapi import FastAPI, HTTPException, Depends, Request, Response
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
        return {'message': 'Succesfull'}
    except HTTPException as e:
        raise e
        

@app.post('/login')
async def login(user: UserModelLogin, Authorize: AuthJWT = Depends()):
    
    login = admin.loginUser(user)
    
    if login:
        token = Authorize.create_access_token(subject=user.username)
        return {'access_token': token}
    raise HTTPException(status_code=401, detail='bad username or password')
    
@app.post('/task')
async def addTask(task: taskModel, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    try:
        id = admin.addTask(task)
        return {'message': f'Succesfull task added with id {id}'}
    except HTTPException as e:
        raise e


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)