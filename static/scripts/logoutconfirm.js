document.getElementById('logoutBtn').addEventListener('click', function () {
    const confirmLogout = confirm('Are you sure you want to log out?');
    if (confirmLogout) {
        // Redirect to the logout route
        window.location.href = '/logout';
    }
});