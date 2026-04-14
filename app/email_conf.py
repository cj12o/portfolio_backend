
from fastapi_mail import ConnectionConfig
from app.conf import settings

conf = ConnectionConfig(
    MAIL_USERNAME = settings.MAIL,
    MAIL_PASSWORD =settings.MAIL_PASSWORD, 
    MAIL_FROM = settings.MAIL,
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME
)