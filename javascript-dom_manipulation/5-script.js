// Select the element with the ID "update_header"
const updateHeaderButton = document.getElementById("update_header");

// Add a click event listener to the "update_header" button
updateHeaderButton.addEventListener("click", function() {
    // Select the header element
    const header = document.querySelector("header");

    // Update the text of the header element
    header.textContent = "New Header!!!";
});
