#!/usr/bin/node
/* prints the addition of two integers */
/* uses a function definition */
function add (a, b) {
  console.log(a + b);
}

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);
add(first, second);
