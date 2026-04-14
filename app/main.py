from fastapi import FastAPI,HTTPException
from fastapi_mail import MessageSchema,MessageType,FastMail
from app.model import EmailReq
from pydantic import NameEmail
from app.email_conf import conf
from app.conf import settings

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"], 
    allow_credentials=True
)

@app.get("/")
async def root():
    return {"message": "running fastapi server"}

@app.get("/health")
async def root():
    return {"message": "running fastapi server 2"}


@app.post("/send-email")
async def send_in_background(data:EmailReq):
    try:
        print(f"✅✅{conf.MAIL_USERNAME}  {conf.MAIL_PASSWORD}   {conf.MAIL_FROM}   {conf.MAIL_PORT}   {conf.MAIL_SERVER}")

        message = MessageSchema(
            subject=f"{data.name} FROM PORTFOLIO",
            recipients=[NameEmail(name=settings.MAIL_USERNAME,email=settings.MAIL)],
            body=data.message,
            subtype=MessageType.plain,
            headers={"Reply-To": data.email}
        )
        
        fm = FastMail(conf)
        
        # This schedules the email to send after the response is sent to the user
        await fm.send_message(message)
        return {"message": "Email has been queued"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))