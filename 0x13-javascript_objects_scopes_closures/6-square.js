#!/usr/bin/node
const S = require('./5-square');
module.exports = class Square extends S {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
