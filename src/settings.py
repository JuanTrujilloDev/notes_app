import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

class Settings:
    # Common settings
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG", False)
    SERVER_NAME = os.getenv("HOST", "127.0.0.1:8000")

    # Database settings
    DATABASE_HOST = os.getenv("DATABASE_HOST", "")
    DATABASE_PORT = os.getenv("DATABASE_PORT", "")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "")
    DATABASE_USER = os.getenv("DATABASE_USER", "")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{db}".format(
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        db=DATABASE_NAME
    )
