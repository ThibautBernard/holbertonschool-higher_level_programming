#!/usr/bin/node
/**
  request GET to the second argument
  and print every characters from this movie
  but in order
  process.argv[2] = the id of the movie
**/

const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};

function test (url) {
  return new Promise((resolve, reject) => {
    request(url, function (err, res, body) {
      if (err) {
        // pass;
      }
      const json = JSON.parse(body);
      resolve(json.name);
    });
  });
}

request(options, function (err, res, body) {
  const json = JSON.parse(body);
  async function t () {
    for (const character of json.characters) {
      const name = await test(character);
      console.log(name);
    }
  }
  t();
  if (err) {
    // pass;
  }
});
