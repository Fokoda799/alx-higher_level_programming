// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Add a click event listener to the <div> element with id "toggle_header"
  $('div#toggle_header').click(function () {
    // Check if the <header> element has the class "red"
    if ($('header').hasClass('red')) {
      // If it has the class "red", remove it and add the class "green"
      $('header').removeClass('red').addClass('green');
    } else {
      // If it doesn't have the class "red", add it and remove the class "green"
      $('header').removeClass('green').addClass('red');
    }
  });
});
