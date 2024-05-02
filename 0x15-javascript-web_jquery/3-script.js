// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Add a click event listener to the <div> element with id "red_header"
  $('div#red_header').click(function () {
    // Add the class "red" to the <header> element
    $('header').addClass('red');
  });
});
