#!/usr/bin/node
/* defines a square that inherits from class rectangle */
const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (c) {
    let i = 1;
    let newer = c;
    if (typeof newer === 'undefined') {
      newer = 'X';
      c = 'X';
    }
    while (i < this.width) {
      newer = newer + c;
      i++;
    }
    i = 0;
    while (i < this.height) {
      console.log(newer);
      i++;
    }
  }
}

module.exports = Square;
