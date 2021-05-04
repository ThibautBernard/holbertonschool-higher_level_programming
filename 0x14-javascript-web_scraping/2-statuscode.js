#!/usr/bin/node
/**
  request GET url and print the status code
  process.argv[2] = the path of the url to request
**/

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (err, res, body) {
  console.log('code:', res.statusCode);
  if (err) {
    // pass;
  }
});
