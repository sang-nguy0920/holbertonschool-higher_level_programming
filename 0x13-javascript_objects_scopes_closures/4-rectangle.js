#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    const exchange = this.width;
    this.width = this.height;
    this.height = exchange;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
