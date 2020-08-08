#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && h > 0)) {
      if ((w > 0)) { this.width = w; }
      if ((h > 0)) { this.height = h; }
    }
  }

  print (w, h) {
    let hei = 0;
    let wei = 0;
    while ((hei !== this.height)) {
      while ((wei !== this.width)) {
        process.stdout.write('X');
        wei++;
      }
      hei++;
      wei = 0;
      console.log();
    }
  }
}

module.exports = Rectangle;
