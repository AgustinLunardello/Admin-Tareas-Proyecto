from pydantic import BaseModel
from hashlib import sha256

class Settings(BaseModel):
    authjwt_secret_key: str = sha256('token'.encode()).hexdigest()
    authjwt_access_token_expires = 3600