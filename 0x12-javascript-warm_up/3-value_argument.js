#!/usr/bin/node
/* prints the value of the argument passed to it */
if (typeof process.argv[2] !== 'undefined') {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
