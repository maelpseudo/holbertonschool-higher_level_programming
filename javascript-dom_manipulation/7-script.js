// Select the <ul> element with the ID "list_movies"
const movieList = document.getElementById("list_movies");

// URL of the Star Wars movies data
const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

// Use the Fetch API to make a GET request to the URL
fetch(apiUrl)
  .then((response) => {
    // Check if the response status is OK (200)
    if (response.status === 200) {
      // Parse the response JSON
      return response.json();
    } else {
      throw new Error("Unable to fetch movie data");
    }
  })
  .then((data) => {
    // Extract the array of movies from the data
    const movies = data.results;

    // Loop through the movies and add each title to the <ul> element
    movies.forEach((movie) => {
      const title = movie.title;
      const listItem = document.createElement("li");
      listItem.textContent = title;
      movieList.appendChild(listItem);
    });
  })
  .catch((error) => {
    console.error("Error:", error);
  });
