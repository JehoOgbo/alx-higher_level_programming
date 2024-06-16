#!/usr/bin/node
/* prints a message depending on number of args */
/* if no args print "No argument", otherwise "Argument found" */
const count = process.argv.length;
if (count === 2) {
  console.log('No argument');
} else  if (count === 3) {
  console.log('Argument found');
} else {
	console.log('Arguments found');
}
