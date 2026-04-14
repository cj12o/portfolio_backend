from pydantic import BaseModel,EmailStr,NameEmail

class EmailReq(BaseModel):
    name:str
    email:EmailStr
    message:str

class EmailRes(BaseModel):

    message:str