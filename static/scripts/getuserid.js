document.addEventListener("DOMContentLoaded", function () {
    // Get all the edit links
    const editLinks = document.querySelectorAll(".edit-link");
    // Attach click event listener to each edit link
    document.addEventListener("DOMContentLoaded", function () {
        // Get all the edit links
        const editLinks = document.querySelectorAll(".edit-link");

        // Attach click event listener to each edit link
        editLinks.forEach(function (editLink) {
            editLink.addEventListener("click", function (event) {
                event.preventDefault();
                const barangayNumber = editLink.dataset.barangayNumber;
                window.location.href = "/barangay_official/residents/edit/" + encodeURIComponent(barangayNumber);
            });
        });
    });
});
