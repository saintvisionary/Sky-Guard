from flask import Blueprint, request, jsonify
from models.user import User, db
from utils.authentication import generate_token, token_required
from utils.logging import log_request
from utils.error_handling import handle_error

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
@log_request
@handle_error
def register():
    # Register a new user
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')

    # Check if the user already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 409

    # Create a new user
    new_user = User(username=username, email=email, role=role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@user_bp.route('/login', methods=['POST'])
@log_request
@handle_error
def login():
    # Authenticate the user
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        token = generate_token(user)
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@user_bp.route('/profile', methods=['GET'])
@token_required
@log_request
@handle_error
def profile(current_user):
    # Return the user's profile information
    return jsonify({
        'username': current_user.username,
        'email': current_user.email,
        'role': current_user.role
    }), 200
