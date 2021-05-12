/**
  request api and add to div character the name request
**/
const $ = window.$;
$(document).ready(() => {
  $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
    $('DIV#character').text(data.name);
  });
});
