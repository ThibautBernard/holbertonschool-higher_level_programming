/**
  update the text within header element when
  someone click on update_header div
**/
const $ = window.$;
$(document).ready(() => {
  $('DIV#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
