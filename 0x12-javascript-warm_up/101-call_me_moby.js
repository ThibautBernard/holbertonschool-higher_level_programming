#!/usr/bin/node
exports.callMeMoby = function (x, MyFunc) {
  let i = 0;
  while (i < x) {
    MyFunc();
    i++;
  }
};
