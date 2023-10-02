```javascript
// Business Plan JavaScript Functions

// Function to create a new business plan
function createPlan() {
    let planData = {
        title: document.getElementById('plan-title').value,
        description: document.getElementById('plan-description').value,
        industry: document.getElementById('plan-industry').value,
        marketAnalysis: document.getElementById('plan-market-analysis').value,
        financialPlan: document.getElementById('plan-financial-plan').value,
    };

    fetch('/api/business_plan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(planData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Business plan created successfully!');
            location.reload();
        } else {
            alert('Error: ' + data.message);
        }
    });
}

// Function to edit an existing business plan
function editPlan(planId) {
    let planData = {
        title: document.getElementById('plan-title').value,
        description: document.getElementById('plan-description').value,
        industry: document.getElementById('plan-industry').value,
        marketAnalysis: document.getElementById('plan-market-analysis').value,
        financialPlan: document.getElementById('plan-financial-plan').value,
    };

    fetch('/api/business_plan/' + planId, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(planData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Business plan updated successfully!');
            location.reload();
        } else {
            alert('Error: ' + data.message);
        }
    });
}

// Function to delete a business plan
function deletePlan(planId) {
    fetch('/api/business_plan/' + planId, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Business plan deleted successfully!');
            location.reload();
        } else {
            alert('Error: ' + data.message);
        }
    });
}
```