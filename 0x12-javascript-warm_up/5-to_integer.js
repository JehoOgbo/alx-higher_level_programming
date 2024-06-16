#!/usr/bin/node
/* converts the argument to a number and prints it */
const number = parseInt(process.argv[2]);/* Number(process.argv[2]); */
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
