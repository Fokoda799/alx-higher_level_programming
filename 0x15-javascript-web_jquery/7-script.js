// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Perform an AJAX request to fetch data from the URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
      // Extract the character name from the response
      const characterName = response.name;
      // Update the content of the <div> element with id "character"
      $('div#character').text(characterName);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      // Handle errors if the request fails
      console.error('Error fetching character name:', textStatus, errorThrown);
    }
  });
});
