#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 1;
    let exes = 'X';
    while (i < this.width) {
      exes = exes + 'X';
      i++;
    }
    i = 0;
    while (i < this.height) {
      console.log(exes);
      i++;
    }
  }
}

module.exports = Rectangle;
