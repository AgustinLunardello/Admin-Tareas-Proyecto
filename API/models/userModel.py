from pydantic import BaseModel
from datetime import datetime
from typing import Union
class UserModelLogin(BaseModel):
    username: str
    password: str

class UserModelRegister(BaseModel):
    name: str
    lastName: str
    bornDate: Union[str, None] = str(datetime.now().strftime('%d-%m-%Y'))
    username: str
    password: str