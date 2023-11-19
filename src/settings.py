import os
from dotenv import load_dotenv

# Settings for the notes app

load_dotenv()

class Settings:

    # Base settings
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = os.environ.get("DEBUG", False)
    SERVER_NAME = "localhost:8000"



def load_settings(settings_class: Settings):
    """
    Turn settings into FLask config values
    :return: config dict
    """
    settings = dict()
    for setting in dir(settings_class):
        if setting.isupper():
            settings[setting] = getattr(settings_class, setting)

    return settings


