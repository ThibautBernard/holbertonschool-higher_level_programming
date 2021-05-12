/**
  script that fetches and prints how to say “Hello” depending on the language
  take the value is entered and request
  to the url the message 'hello' in then language
  entered by the user
  Or when the focus is on div language_code
  language : es, fr, eng
**/
const $ = window.$;
$(document).ready(() => {
  $('INPUT#language_code').focus(() => {
    const language = $('INPUT#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + language, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#btn_translate').click(() => {
    const language = $('INPUT#language_code').val();
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + language, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
