// Select the elements
const toggleHeader = document.getElementById("toggle_header");
const header = document.querySelector("header");

// Add a click event listener to the "toggle_header" element
toggleHeader.addEventListener("click", function() {
    // Check the current class of the header
    if (header.classList.contains("red")) {
        // If it has the "red" class, remove it and add the "green" class
        header.classList.remove("red");
        header.classList.add("green");
    } else {
        // If it has the "green" class (or no class), remove it and add the "red" class
        header.classList.remove("green");
        header.classList.add("red");
    }
});
