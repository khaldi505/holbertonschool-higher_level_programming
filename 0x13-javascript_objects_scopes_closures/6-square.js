#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let hei = 0;
    if ((typeof (c) === 'undefined')) { c = 'X'; }
    while ((hei !== this.height)) {
      let wei = 0;
      while ((wei !== this.width)) {
        process.stdout.write(c);
        wei++;
      }
      hei++;
      console.log();
    }
  }
}

module.exports = Square;
