```python
from flask import Blueprint, request, jsonify
from src.services.business_plan_service import create_plan, edit_plan, delete_plan

business_plan = Blueprint('business_plan', __name__)

@business_plan.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    result = create_plan(data)
    if result:
        return jsonify({"message": "plan_saved", "data": result}), 201
    else:
        return jsonify({"message": "Error in saving plan"}), 400

@business_plan.route('/edit/<plan_id>', methods=['PUT'])
def edit(plan_id):
    data = request.get_json()
    result = edit_plan(plan_id, data)
    if result:
        return jsonify({"message": "plan_saved", "data": result}), 200
    else:
        return jsonify({"message": "Error in editing plan"}), 400

@business_plan.route('/delete/<plan_id>', methods=['DELETE'])
def delete(plan_id):
    result = delete_plan(plan_id)
    if result:
        return jsonify({"message": "plan_deleted"}), 200
    else:
        return jsonify({"message": "Error in deleting plan"}), 400
```