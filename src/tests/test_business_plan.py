```python
import unittest
from src.models.business_plan import BusinessPlan
from src.services.business_plan_service import create_plan, edit_plan, delete_plan

class TestBusinessPlan(unittest.TestCase):

    def setUp(self):
        self.plan_data = {
            'title': 'Test Plan',
            'description': 'This is a test plan',
            'industry': 'Tech',
            'market_analysis': 'Test market analysis',
            'financial_plan': 'Test financial plan'
        }
        self.plan = create_plan(self.plan_data)

    def test_create_plan(self):
        self.assertIsInstance(self.plan, BusinessPlan)
        self.assertEqual(self.plan.title, self.plan_data['title'])
        self.assertEqual(self.plan.description, self.plan_data['description'])
        self.assertEqual(self.plan.industry, self.plan_data['industry'])
        self.assertEqual(self.plan.market_analysis, self.plan_data['market_analysis'])
        self.assertEqual(self.plan.financial_plan, self.plan_data['financial_plan'])

    def test_edit_plan(self):
        new_data = {
            'title': 'Updated Test Plan',
            'description': 'This is an updated test plan',
            'industry': 'Healthcare',
            'market_analysis': 'Updated market analysis',
            'financial_plan': 'Updated financial plan'
        }
        updated_plan = edit_plan(self.plan.id, new_data)
        self.assertEqual(updated_plan.title, new_data['title'])
        self.assertEqual(updated_plan.description, new_data['description'])
        self.assertEqual(updated_plan.industry, new_data['industry'])
        self.assertEqual(updated_plan.market_analysis, new_data['market_analysis'])
        self.assertEqual(updated_plan.financial_plan, new_data['financial_plan'])

    def test_delete_plan(self):
        delete_plan(self.plan.id)
        self.assertIsNone(BusinessPlan.query.get(self.plan.id))

if __name__ == '__main__':
    unittest.main()
```