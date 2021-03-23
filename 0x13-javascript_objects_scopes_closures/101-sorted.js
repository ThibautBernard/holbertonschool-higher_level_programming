#!/usr/bin/node
const d = require('./101-data').dict;
const newD = {};
for (const key in d) {
  if (d[key] in newD) {
    newD[d[key]].push(key);
  } else {
    newD[d[key]] = [key];
  }
}
console.log(newD);
