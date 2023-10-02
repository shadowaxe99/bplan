```python
import jwt
from datetime import datetime, timedelta
from src.config import config

def generate_token(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(
        payload,
        config.SECRET_KEY,
        algorithm='HS256'
    )

def decode_token(token):
    try:
        payload = jwt.decode(token, config.SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise Exception('Signature expired. Please log in again.')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token. Please log in again.')
```