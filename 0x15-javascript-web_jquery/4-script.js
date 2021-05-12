/**
    Select the header and add a class (red) in the case
    where the header don't have a class
    In the case of someone click on the toggle div,
    the class name of the header is change to (red -> green or green -> red)
**/
const $ = window.$;
$(document).ready(() => {
  const header = $('header');
  const nameClassHeader = header.attr('class');
  if (!nameClassHeader) {
    header.addClass('red');
  }
  $('DIV#toggle_header').click(() => {
    if (nameClassHeader === 'green') {
      header.attr('class', 'red');
    } else {
      header.attr('class', 'green');
    }
  });
});
