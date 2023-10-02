```python
import unittest
from src.services.authentication_service import login_user, signup_user, reset_password
from src.models.user import User

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "password": "testpassword"
        }

    def test_login_user(self):
        response = login_user(self.user_data["email"], self.user_data["password"])
        self.assertEqual(response["message"], "login_success")

    def test_signup_user(self):
        response = signup_user(self.user_data)
        self.assertEqual(response["message"], "signup_success")

    def test_reset_password(self):
        response = reset_password(self.user_data["email"])
        self.assertEqual(response["message"], "password_reset_success")

if __name__ == '__main__':
    unittest.main()
```