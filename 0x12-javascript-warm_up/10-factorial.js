#!/usr/bin/node
let nb = parseInt(process.argv[2]);
if (isNaN(nb)) {
  nb = 1;
}
function factor (nb) {
  if (nb <= 1) {
    return (1);
  }
  return nb * factor(nb - 1);
}
console.log(factor(nb));
