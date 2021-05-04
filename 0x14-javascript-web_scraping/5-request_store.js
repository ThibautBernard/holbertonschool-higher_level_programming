#!/usr/bin/node
/**
  request GET to the second argument
  and write into a file
  process.argv[2] = the path of the url
  process.argv[3] = file to write
**/

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};
const fs = require('fs');

request(options, function (err, res, body) {
  fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
    if (err) {
      // pass;
    }
  });
  if (err) {
    // pass;
  }
});
