```python
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from src.services.business_plan_service import get_all_plans

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def show_dashboard():
    plans = get_all_plans(current_user.id)
    return render_template('dashboard.html', plans=plans)

@dashboard.route('/dashboard/delete/<int:plan_id>', methods=['POST'])
@login_required
def delete_plan(plan_id):
    try:
        delete_plan(current_user.id, plan_id)
        flash('Plan deleted successfully', 'plan_deleted')
    except Exception as e:
        flash(str(e), 'error')
    return redirect(url_for('dashboard.show_dashboard'))
```