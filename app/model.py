from pydantic import BaseModel,EmailStr

class EmailReq(BaseModel):
    name:str
    email:EmailStr
    message:str

    