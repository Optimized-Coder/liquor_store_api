from ..models import APIUser
from flask import request

def check_api_key():
    users = APIUser.query.all()
    for user in users:
        if user.api_key == request.headers.get('x-api-key'):
            return True
    return False