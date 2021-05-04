#!/usr/bin/node
/**
  request GET to swap-api
  return the number of movie for a specific user
  process.argv[2] = the path of the url
**/

/**
  compare for each iteration of filter
  each element of the array
  value: element of the array
 **/
function compare (value) {
  if (value === 'https://swapi-api.hbtn.io/api/people/18/') {
    return (value);
  }
}
const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (err, res, body) {
  const json = JSON.parse(body);
  const arr = [];
  if (err) {
    console.log(err);
  } else {
    for (const k of json.results) {
      /**
        filter, compare each value of the array and return array
        filled if the comparaison is true
      **/
      const tmp = k.characters.filter(compare);
      if (tmp.length > 0) {
        arr.push(tmp);
      }
    }
    console.log(arr.length);
  }
});
