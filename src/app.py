from flask import Flask

from dependencies import db, migrate
from modules.users.urls import users_blueprint

app = Flask(__name__)
app.config.from_object('settings.Settings')
db.init_app(app)
migrate.init_app(app, db)
app.app_context().push()
app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run()
