from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Database init
db = SQLAlchemy()
migrate = Migrate()
