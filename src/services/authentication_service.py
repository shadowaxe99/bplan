```python
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from src.models.user import User
from src.utils.email_service import send_email
from src.utils.password_service import hash_password
from src.utils.token_service import generate_token

def login(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return True, "login_success"
    return False, "Invalid email or password"

def signup(name, email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        return False, "Email already registered"
    hashed_password = hash_password(password)
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    send_email(email, "Welcome to AutoBizPlanGen", "signup_success")
    return True, "signup_success"

def reset_password(email):
    user = User.query.filter_by(email=email).first()
    if not user:
        return False, "Email not registered"
    new_password = generate_token()
    hashed_password = hash_password(new_password)
    user.password = hashed_password
    db.session.commit()
    send_email(email, "Password Reset", "password_reset_success", new_password)
    return True, "password_reset_success"
```