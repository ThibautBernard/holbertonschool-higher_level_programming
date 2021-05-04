#!/usr/bin/node
/**
  request GET to the second argument
  and print every characters from this movie
  process.argv[2] = the id of the movie
**/

const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};

request(options, function (err, res, body) {
  const json = JSON.parse(body);
  for (const character of json.characters) {
    request(character, function (err, res, body) {
      if (err) {
        // pass;
      }
      const json = JSON.parse(body);
      console.log(json.name);
    });
  }
  if (err) {
    // pass;
  }
});
