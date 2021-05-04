#!/usr/bin/node
/**
  write into a file
  process.argv[2] = file path / name
  process.argv[3] = content
**/

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
