import jwt
from flask import request, jsonify
from functools import wraps
from models.user import User
from config import Config

def token_required(f):
    # Decorator to ensure the user is authenticated
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
            current_user = User.query.filter_by(username=data['username']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

def generate_token(user):
    # Generate a JWT token for the user
    token = jwt.encode({'username': user.username, 'role': user.role}, Config.JWT_SECRET_KEY, algorithm="HS256")
    return token
