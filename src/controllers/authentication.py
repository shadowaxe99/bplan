```python
from flask import Blueprint, request, jsonify, make_response
from src.services.authentication_service import login_user, signup_user, reset_password
from src.utils.token_service import generate_token

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = login_user(data['email'], data['password'])
    if user:
        token = generate_token(user)
        return make_response(jsonify({'token': token, 'message': 'login_success'}), 200)
    return make_response(jsonify({'message': 'Invalid credentials'}), 401)

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user = signup_user(data['name'], data['email'], data['password'])
    if user:
        token = generate_token(user)
        return make_response(jsonify({'token': token, 'message': 'signup_success'}), 201)
    return make_response(jsonify({'message': 'Email already exists'}), 400)

@auth.route('/reset-password', methods=['POST'])
def password_reset():
    data = request.get_json()
    user = reset_password(data['email'])
    if user:
        return make_response(jsonify({'message': 'password_reset_success'}), 200)
    return make_response(jsonify({'message': 'Email does not exist'}), 400)
```