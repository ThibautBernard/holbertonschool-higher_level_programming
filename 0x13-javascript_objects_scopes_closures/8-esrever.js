#!/usr/bin/node
exports.esrever = function (list) {
  const aRevert = [];
  for (let i = list.length - 1; i >= 0; i--) {
    aRevert.push(list[i]);
  }
  return aRevert;
};
