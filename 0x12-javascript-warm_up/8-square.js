#!/usr/bin/node
const nb = parseInt(process.argv[2]);
let i = 0;
if (isNaN(nb)) {
  console.log('Missing size');
} else {
  while (i < nb) {
    console.log('X'.repeat(nb));
    i++;
  }
}
