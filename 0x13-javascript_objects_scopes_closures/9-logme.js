#!/usr/bin/node
/* prints the number of args printed and the new arg value */
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
