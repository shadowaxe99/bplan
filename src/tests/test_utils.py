```python
import unittest
from src.utils import email_service, password_service, token_service

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.email = "test@example.com"
        self.password = "password123"
        self.token = "token123"

    def test_send_email(self):
        result = email_service.send_email(self.email, "Test Subject", "Test Message")
        self.assertTrue(result)

    def test_hash_password(self):
        hashed_password = password_service.hash_password(self.password)
        self.assertNotEqual(self.password, hashed_password)

    def test_generate_token(self):
        token = token_service.generate_token(self.email)
        self.assertIsNotNone(token)

    def test_verify_token(self):
        token = token_service.generate_token(self.email)
        email = token_service.verify_token(token)
        self.assertEqual(email, self.email)

if __name__ == '__main__':
    unittest.main()
```