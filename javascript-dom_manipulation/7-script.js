// request to the starwars API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
// async (promise) waiting once server responds woith headers
  .then(function (response) {
    // converts json to JS object and async (promise)
    return response.json();
  })
  // once json finishes. receives JS object
  .then(function (data) {
    // select the ul element with id= list_movies
    const movies = document.querySelector('#list_movies');
    // loop through array of movie objects stored in data.results
    data.results.forEach(function (movie) {
      // create new li element for current movie
      const items = document.createElement('li');
      // set the li text to the movie title
      items.textContent = movie.title;
      // append li insude list_movies
      movies.appendChild(items);
    });
  });
