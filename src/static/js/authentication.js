```javascript
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;
        loginUser(email, password);
    });

    signupForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const name = document.getElementById('signup-name').value;
        const email = document.getElementById('signup-email').value;
        const password = document.getElementById('signup-password').value;
        signupUser(name, email, password);
    });
});

function loginUser(email, password) {
    fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'login_success') {
            window.location.href = '/dashboard';
        } else {
            alert(data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function signupUser(name, email, password) {
    fetch('/api/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, password }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'signup_success') {
            window.location.href = '/dashboard';
        } else {
            alert(data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
```