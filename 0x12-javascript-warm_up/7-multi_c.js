#!/usr/bin/node
const nb = parseInt(process.argv[2]);
let i = 0;
if (isNaN(nb)) {
  console.log('Missing number of occurrences');
} else {
  while (i < nb) {
    console.log('C is fun');
    i++;
  }
}
