//Select the element with the ID "character"
const characterElement = document.getElementById("character");

// URL of the Star Wars character data
const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";

// Use the Fetch API to make a GET request to the URL
fetch(apiUrl)
  .then((response) => {
    // Check if the response status is OK (200)
    if (response.status === 200) {
      // Parse the response JSON
      return response.json();
    } else {
      throw new Error("Unable to fetch character data");
    }
  })
  .then((data) => {
    // Extract the character name from the data
    const characterName = data.name;

    // Update the content of the "character" element with the character name
    characterElement.textContent = characterName;
  })
  .catch((error) => {
    console.error("Error:", error);
  }); 
