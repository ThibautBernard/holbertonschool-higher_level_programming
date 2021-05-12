/**
    Select the header and change the font color of the header text when
    someone click on the div #read_header
**/
const $ = window.$;
$(document).ready(() => {
  $('DIV#red_header').click(() => {
    const header = $('header');
    header.addClass('red');
  });
});
