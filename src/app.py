from flask import Flask
from werkzeug.exceptions import HTTPException

from urls import load_urls
from settings import Settings, load_settings
from error_handling import handle_exception

app = Flask(__name__)

# Load urls
load_urls(app)

# Load settings
settings = Settings()
app.config.update(load_settings(settings))

# Custom error handling
app.errorhandler(HTTPException)(handle_exception)

if __name__ == '__main__':
    app.run()