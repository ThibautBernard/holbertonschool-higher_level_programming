#!/usr/bin/node
function check (array, low, max) {
  const pivot = array[max];
  let i = low - 1;
  let y = low;
  while (y < max) {
    if (array[y] < pivot) {
      i++;
      const tmp = array[i];
      array[i] = array[y];
      array[y] = tmp;
    }
    y++;
  }
  i++;
  const tmp = array[i];
  array[i] = array[max];
  array[max] = tmp;
  return (i);
}
function quick (array, low, high) {
  if (low < high) {
    const p = check(array, low, high);
    quick(array, low, p - 1);
    quick(array, p + 1, high);
  }
}

const nbArgs = process.argv.length;
if (nbArgs === 2) {
  console.log(0);
} else if (nbArgs === 3) {
  console.log(0);
} else {
  const newArray = process.argv.slice(2, nbArgs);
  const length = newArray.length;
  const aToInt = newArray.map(i => Number(i));
  quick(aToInt, 0, length - 1);
  console.log(aToInt[length - 2]);
}
