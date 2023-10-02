```python
from src.models.business_plan import BusinessPlan
from src.models.user import User
from src import db

def create_plan(user_id, plan_data):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    new_plan = BusinessPlan(
        title=plan_data['title'],
        content=plan_data['content'],
        user_id=user_id
    )

    db.session.add(new_plan)
    db.session.commit()

    return {"message": "Business plan created successfully"}, 201

def get_all_plans(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    plans = BusinessPlan.query.filter_by(user_id=user_id).all()
    return {"plans": [plan.to_dict() for plan in plans]}, 200

def get_plan(user_id, plan_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    plan = BusinessPlan.query.get(plan_id)
    if not plan or plan.user_id != user_id:
        return {"error": "Plan not found"}, 404

    return {"plan": plan.to_dict()}, 200

def update_plan(user_id, plan_id, plan_data):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    plan = BusinessPlan.query.get(plan_id)
    if not plan or plan.user_id != user_id:
        return {"error": "Plan not found"}, 404

    plan.title = plan_data.get('title', plan.title)
    plan.content = plan_data.get('content', plan.content)

    db.session.commit()

    return {"message": "Business plan updated successfully"}, 200

def delete_plan(user_id, plan_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    plan = BusinessPlan.query.get(plan_id)
    if not plan or plan.user_id != user_id:
        return {"error": "Plan not found"}, 404

    db.session.delete(plan)
    db.session.commit()

    return {"message": "Business plan deleted successfully"}, 200
```