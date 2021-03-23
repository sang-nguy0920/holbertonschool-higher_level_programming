#!/usr/bin/node

const SquareNew = require('./5-square');

module.exports = class Square extends SquareNew {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 0; x < this.width; x++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
