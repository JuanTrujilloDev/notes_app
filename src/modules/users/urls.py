from flask import Blueprint

from modules.users.views import create_user

users_blueprint = Blueprint('users', __name__, url_prefix='/users/')

users_blueprint.add_url_rule('', view_func=create_user, methods=['POST'])