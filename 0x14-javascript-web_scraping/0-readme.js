#!/usr/bin/node
/**
  read a file and print his content
**/

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
