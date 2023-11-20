from flask import request, jsonify

from modules.users.models import User

def create_user():
    request_data = request.get_json()
    user = User(**request_data)
    user.save()
    return jsonify(request_data), 201