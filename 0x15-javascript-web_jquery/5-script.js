/**
  add new <li> to ul when someone click on add_item div
**/
const $ = window.$;
$(document).ready(() => {
  $('DIV#add_item').click(() => {
    const ul = $('UL.my_list');
    ul.append('<li>Item</li>');
  });
});
