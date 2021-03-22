#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const nb = parseInt(process.argv[2]);
const nbDeux = parseInt(process.argv[3]);
console.log(add(nb, nbDeux));
