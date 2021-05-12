/**
  take the value is entered and request
  to the url the message 'hello' in then language
  entered by the user
  language : es, fr, eng
**/
const $ = window.$;
$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const language = $('INPUT#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + language, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
