#!/usr/bin/node
const nbArgs = process.argv.length;
if (nbArgs === 2) {
  console.log('No argument');
} else if (nbArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
