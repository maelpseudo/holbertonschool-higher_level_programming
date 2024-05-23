// Select the element with the ID "red_header"
const redHeader = document.getElementById("red_header");

// Add a click event listener to the "red_header" element
redHeader.addEventListener("click", function() {
    // Select the header element
    const header = document.querySelector("header");

    // Add the "red" class to the header element
    header.classList.add("red");
});
