#!/usr/bin/node
const nbArgs = process.argv.length;
if (nbArgs === 2) {
  console.log('Not a number');
} else if (nbArgs === 3) {
  const nb = parseInt(process.argv[2]);
  if (isNaN(nb)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + nb);
  }
}
