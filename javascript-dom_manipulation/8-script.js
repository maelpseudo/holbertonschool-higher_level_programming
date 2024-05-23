// Select the element with the ID "hello"
const helloElement = document.getElementById("hello");

// URL for fetching the translation of "hello" in French
const apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

document.addEventListener("DOMContentLoaded", function () {
  // Use the Fetch API to make a GET request to the URL
  fetch(apiUrl)
    .then((response) => {
      // Check if the response status is OK (200)
      if (response.status === 200) {
        // Parse the response text (translation) as JSON
        return response.json();
      } else {
        throw new Error("Unable to fetch translation");
      }
    })
    .then((data) => {
      // Display the translation in the "hello" element
      helloElement.textContent = data.hello;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
