#!/usr/bin/node
/**
  request GET to the second argument
  and print a dict of number of task completed
  by user_id
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
  let tmpUserId = 1;
  const di = {};
  for (const k of json) {
    if (k.userId === tmpUserId && k.completed) {
      counter += 1;
    } else if (tmpUserId !== k.userId) {
      di[tmpUserId] = counter;
      if (k.completed) {
        counter = 1;
      } else {
        counter = 0;
      }
    }
    tmpUserId = k.userId;
  }
  di[tmpUserId] = counter;
  console.log(di);
  if (err) {
    // pass;
  }
});
