// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Perform an AJAX request to fetch data from the URL
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (response) {
      // Extract the translation of "hello" from the response
      const helloTranslation = response.hello;
      // Update the content of the <div> element with id "hello"
      $('div#hello').text(helloTranslation);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      // Handle errors if the request fails
      console.error('Error fetching hello translation:', textStatus, errorThrown);
    }
  });
});
