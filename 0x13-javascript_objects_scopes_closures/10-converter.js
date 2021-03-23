#!/usr/bin/node
exports.converter = function (base) {
  return function convert (nb) {
    return (nb.toString(base));
  };
};
