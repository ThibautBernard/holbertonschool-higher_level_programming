#!/usr/bin/node

module.exports = function callMeMoby (x, MyFunc) {
  let i = 0;
  while (i < x) {
    callMeMoby();
    i++;
  }
};
