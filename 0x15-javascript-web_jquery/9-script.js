/**
  request api and add to div hello the hello message fetch
**/
const $ = window.$;
$(document).ready(() => {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
    $('DIV#hello').text(data.hello);
  });
});
