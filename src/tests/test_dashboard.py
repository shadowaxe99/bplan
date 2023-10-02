```python
import unittest
from unittest.mock import patch
from src.controllers.dashboard import get_dashboard
from src.models.user import User
from src.models.business_plan import BusinessPlan

class TestDashboard(unittest.TestCase):

    @patch('src.controllers.dashboard.db')
    def test_get_dashboard(self, mock_db):
        # Mock user and business plan data
        mock_user = User(id=1, name='Test User', email='testuser@example.com')
        mock_plan = BusinessPlan(id=1, user_id=1, status='Draft', content='Test Content')

        # Mock the session query
        mock_db.session.query.return_value.filter.return_value.all.return_value = [mock_plan]

        # Call the function
        result = get_dashboard(mock_user)

        # Assert the function returns the correct data
        self.assertEqual(result, [mock_plan])

        # Assert the function calls the database with correct parameters
        mock_db.session.query.assert_called_with(BusinessPlan)
        mock_db.session.query.return_value.filter.assert_called_with(BusinessPlan.user_id == mock_user.id)

if __name__ == '__main__':
    unittest.main()
```