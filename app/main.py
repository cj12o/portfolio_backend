from fastapi import FastAPI
from app.model import EmailReq



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/mail")
async def mail(data:EmailReq):
    print(data)
    return {"message": "Hello World"}