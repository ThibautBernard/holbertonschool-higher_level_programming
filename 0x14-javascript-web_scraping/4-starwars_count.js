#!/usr/bin/node
/**
  request GET to swap-api
  return the number of movie for a specific user
  process.argv[2] = the path of the url
**/

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (err, res, body) {
  const json = JSON.parse(body);
  let counter = 0;
  for (const k of json.results) {
    for (const url of k.characters) {
      if (url === 'https://swapi-api.hbtn.io/api/people/18/') {
        counter += 1;
      }
    }
  }
  console.log(counter);
  if (err) {
    // pass;
  }
});
