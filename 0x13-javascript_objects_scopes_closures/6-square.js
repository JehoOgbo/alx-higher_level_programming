#!/usr/bin/node
/* defines a square that inherits from class rectangle */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    let i = 1;
    let newer = c;
	if (typeof newer === "undefined") {
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
