#!/usr/bin/node
/**
  request GET to swap-api
  process.argv[2] = the path of the id of the film
**/

const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};

request(options, function (err, res, body) {
  const json = JSON.parse(body);
  console.log(json.title);
  if (err) {
    // pass;
  }
});
