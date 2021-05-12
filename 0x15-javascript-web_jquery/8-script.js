/**
  request api and add to div list_movies all movies
**/
const $ = window.$;
$(document).ready(() => {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    for (const Movie of data.results) {
      $('UL#list_movies').append('<li>' + Movie.title + '</li>');
    }
  });
});
