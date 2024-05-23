// Select the element with the ID "red_header"
const redHeader = document.getElementById("red_header");

// Add a click event to the element
redHeader.addEventListener("click", function() {
    // Select the header element
    const header = document.querySelector("header");

    // Change the text color of the header to red
    header.style.color = "#FF0000";
});
