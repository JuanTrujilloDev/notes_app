from flask import request

def login():
    print(request.get_json())
    return 'Login page'