from pydantic import BaseModel

class User(BaseModel):
    Username: str
    email: str
    password: str