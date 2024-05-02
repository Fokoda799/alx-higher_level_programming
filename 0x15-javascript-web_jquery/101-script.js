// Wait for the DOM to be fully loaded
$(document).ready(function () {
  // Add click event listener to the button with id "add_item"
  $('#add_item').click(function () {
    // Create a new <li> element
    const newItem = $('<li>').text('Item');
    // Append the new <li> element to the <ul> with class "my_list"
    $('ul.my_list').append(newItem);
  });

  // Add click event listener to the button with id "remove_item"
  $('#remove_item').click(function () {
    // Remove the last <li> element from the <ul> with class "my_list"
    $('ul.my_list li:last-child').remove();
  });

  // Add click event listener to the button with id "clear_list"
  $('#clear_list').click(function () {
    // Remove all <li> elements from the <ul> with class "my_list"
    $('ul.my_list').empty();
  });
});
