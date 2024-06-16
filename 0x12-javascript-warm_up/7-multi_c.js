#!/usr/bin/node
/* prints a text string x times */
const x = Number(process.argv[2]);
let i = 0;
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
