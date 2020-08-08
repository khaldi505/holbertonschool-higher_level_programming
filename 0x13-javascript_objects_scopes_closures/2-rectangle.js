#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && h > 0)) {
      if ((w > 0)) { this.width = w; }
      if ((h > 0)) { this.height = h; }
    }
  }
}
module.exports = Rectangle;
