from pydantic import BaseModel
from datetime import datetime

class UserModelLogin(BaseModel):
    username: str
    password: str

class UserModelRegister(BaseModel):
    name: str
    lastName: str
    bornDate: str = str(datetime.now().strftime('%d-%m-%Y'))
    username: str
    password: str