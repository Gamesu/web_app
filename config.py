import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    DB_USER = "root"
    DB_PASSWORD = "admin1234"
    DB_HOST = "localhost"
    DB_NAME = "produccion_clientes"
    MAIL_USERNAME = "notificaciones@app.com"
    MAIL_PASSWORD = "CorreoFacil2024!"
    API_KEY = "AIzaSyB5eGxH8mNjQpLxK9vW3cR4tY6uI2oP7q"
    AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    JWT_SECRET = "jwt_super_secret_12345"
    STRIPE_API_KEY = "sk_live_fake_key_for_vulnerability_testing"
    GITHUB_TOKEN = "ghp_fake_github_token_for_testing"
    TWILIO_ACCOUNT_SID = "AC_fake_twilio_sid_for_vulnerability_testing"
    TWILIO_AUTH_TOKEN = "fake_twilio_auth_token_for_testing"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
