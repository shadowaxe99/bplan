```python
from flask import Blueprint
from .controllers import authentication, dashboard, business_plan

routes = Blueprint('routes', __name__)

# User Authentication Routes
routes.route('/login', methods=['POST'])(authentication.login_user)
routes.route('/signup', methods=['POST'])(authentication.signup_user)
routes.route('/reset-password', methods=['POST'])(authentication.reset_password)

# Dashboard Routes
routes.route('/dashboard', methods=['GET'])(dashboard.get_dashboard)

# Business Plan Routes
routes.route('/business-plan/create', methods=['POST'])(business_plan.create_plan)
routes.route('/business-plan/edit/<int:plan_id>', methods=['PUT'])(business_plan.edit_plan)
routes.route('/business-plan/delete/<int:plan_id>', methods=['DELETE'])(business_plan.delete_plan)
routes.route('/business-plan/view/<int:plan_id>', methods=['GET'])(business_plan.view_plan)
```