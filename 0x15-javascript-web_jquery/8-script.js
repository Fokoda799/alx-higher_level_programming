// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Perform an AJAX request to fetch data from the URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
      // Iterate over each movie in the response
      $.each(response.results, function (index, movie) {
        // Extract the title of the movie
        const title = movie.title;
        // Create a new <li> element with the movie title
        const listItem = $('<li>').text(title);
        // Append the <li> element to the <ul> with id "list_movies"
        $('ul#list_movies').append(listItem);
      });
    },
    error: function (jqXHR, textStatus, errorThrown) {
      // Handle errors if the request fails
      console.error('Error fetching movies:', textStatus, errorThrown);
    }
  });
});
