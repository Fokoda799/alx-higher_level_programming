// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Function to fetch translation when Enter key is pressed
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) { // 13 is the Enter key code
      fetchTranslation();
    }
  });

  // Add click event listener to the button with id "btn_translate"
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  // Function to fetch translation from API
  function fetchTranslation () {
    // Get the language code entered by the user from the input with id "language_code"
    const languageCode = $('#language_code').val();

    // Perform an AJAX request to fetch translation from the API service
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      method: 'GET',
      data: { lang: languageCode }, // Pass the language code as query parameter
      dataType: 'json',
      success: function (response) {
        // Update the content of the <div> with id "hello" with the translation
        $('#hello').text(response.hello);
      },
      error: function (jqXHR, textStatus, errorThrown) {
        // Handle errors if the request fails
        console.error('Error fetching translation:', textStatus, errorThrown);
      }
    });
  }
});
