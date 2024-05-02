$(document).ready(function () {
  // Add a click event listener to the <div> element with id "red_header"
  $('div#red_header').click(function () {
    // Update the text color of the <header> element to red (#FF0000)
    $('header').css('color', '#FF0000');
  });
});
