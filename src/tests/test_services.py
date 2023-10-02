```python
import unittest
from src.services.authentication_service import login_user, signup_user, reset_password
from src.services.business_plan_service import create_plan, edit_plan, delete_plan

class TestServices(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        self.plan_data = {
            'title': 'Test Plan',
            'description': 'This is a test plan',
            'content': 'Test plan content'
        }

    def test_login_user(self):
        response = login_user(self.user_data['email'], self.user_data['password'])
        self.assertEqual(response['message'], 'login_success')

    def test_signup_user(self):
        response = signup_user(self.user_data)
        self.assertEqual(response['message'], 'signup_success')

    def test_reset_password(self):
        response = reset_password(self.user_data['email'])
        self.assertEqual(response['message'], 'password_reset_success')

    def test_create_plan(self):
        response = create_plan(self.plan_data)
        self.assertEqual(response['message'], 'plan_saved')

    def test_edit_plan(self):
        response = edit_plan(self.plan_data['title'], self.plan_data)
        self.assertEqual(response['message'], 'plan_saved')

    def test_delete_plan(self):
        response = delete_plan(self.plan_data['title'])
        self.assertEqual(response['message'], 'plan_deleted')

if __name__ == '__main__':
    unittest.main()
```