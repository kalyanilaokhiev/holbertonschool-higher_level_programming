// request to the starwars API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
// async (promise) waiting once server responds woith headers
  .then(function (response) {
    // converts json to JS object and async (promise)
    return response.json();
  })
  // once json finishes. receives JS object
  .then(function (data) {
    // selects tag with is = charcter and displays name
    document.querySelector('#character').textContent = data.name;
  });
