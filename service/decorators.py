import jwt
from flask import request, current_app

from implemented import user_service


def auth_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.environ.get("HTTP_AUTHORIZATION").replace('Bearer ', '')

        if not token:
            raise Exception

        try:
            jwt.decode(token, key=current_app.config["SECRET_KEY"],
                              algorithms=current_app.config["ALGORITHM"])
            return func(*args, **kwargs)

        except Exception as e:
            raise e

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.environ.get("HTTP_AUTHORIZATION").replace('Bearer ', '')

        if not token:
            return 'Токен не пришел'

        try:
            data = jwt.decode(token, key=current_app.config["SECRET_KEY"],
                              algorithms=current_app.config["ALGORITHM"])

            if user_service.user_by_username(data['username']).role == 'admin':
                return func(*args, **kwargs)

            else:
                return "Нет прав"

        except Exception as e:
            raise e

    return wrapper