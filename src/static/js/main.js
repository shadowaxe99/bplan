```javascript
// src/static/js/main.js

document.addEventListener('DOMContentLoaded', (event) => {
    // Code to run after the DOM is fully loaded

    // Login form submission
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            loginUser(email, password);
        });
    }

    // Signup form submission
    const signupForm = document.getElementById('signup-form');
    if (signupForm) {
        signupForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            signupUser(name, email, password);
        });
    }

    // Dashboard actions
    const dashboard = document.getElementById('dashboard');
    if (dashboard) {
        const editButtons = document.getElementsByClassName('edit-button');
        const deleteButtons = document.getElementsByClassName('delete-button');
        const shareButtons = document.getElementsByClassName('share-button');

        Array.from(editButtons).forEach((button) => {
            button.addEventListener('click', (e) => {
                const planId = e.target.dataset.planId;
                editPlan(planId);
            });
        });

        Array.from(deleteButtons).forEach((button) => {
            button.addEventListener('click', (e) => {
                const planId = e.target.dataset.planId;
                deletePlan(planId);
            });
        });

        Array.from(shareButtons).forEach((button) => {
            button.addEventListener('click', (e) => {
                const planId = e.target.dataset.planId;
                sharePlan(planId);
            });
        });
    }
});
```