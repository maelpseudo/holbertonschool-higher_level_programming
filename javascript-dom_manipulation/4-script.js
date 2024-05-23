//Select the element with the ID "add_item"
const addItemButton = document.getElementById("add_item");

// Select the list with the class "my_list"
const myList = document.querySelector(".my_list");

// Add a click event listener to the "add_item" button
addItemButton.addEventListener("click", function() {
    // Create a new <li> element
    const newListItem = document.createElement("li");

    // Set the content of the new element
    newListItem.textContent = "Item";

    // Append the new element to the list
    myList.appendChild(newListItem);
}); 
