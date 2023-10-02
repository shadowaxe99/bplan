```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    loadDashboard();
});

function loadDashboard() {
    fetch('/api/dashboard', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        displayPlans(data.plans);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function displayPlans(plans) {
    const dashboard = document.getElementById('dashboard');
    dashboard.innerHTML = '';

    plans.forEach(plan => {
        const planElement = document.createElement('div');
        planElement.className = 'plan';

        const title = document.createElement('h3');
        title.textContent = plan.title;
        planElement.appendChild(title);

        const status = document.createElement('p');
        status.textContent = `Status: ${plan.status}`;
        planElement.appendChild(status);

        const editButton = document.createElement('button');
        editButton.textContent = 'Edit';
        editButton.addEventListener('click', () => editPlan(plan.id));
        planElement.appendChild(editButton);

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', () => deletePlan(plan.id));
        planElement.appendChild(deleteButton);

        const shareButton = document.createElement('button');
        shareButton.textContent = 'Share';
        shareButton.addEventListener('click', () => sharePlan(plan.id));
        planElement.appendChild(shareButton);

        dashboard.appendChild(planElement);
    });
}

function editPlan(planId) {
    window.location.href = `/edit_plan/${planId}`;
}

function deletePlan(planId) {
    fetch(`/api/delete_plan/${planId}`, {
        method: 'DELETE',
    })
    .then(() => {
        loadDashboard();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function sharePlan(planId) {
    // Implement share functionality
}
```