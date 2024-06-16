#!/usr/bin/node
/* prints a square */
const x = process.argv[2];
if (isNaN(x)) {
	console.log("Missing size");
}
let row = 0;
let column = 1;
let exes = 'X';
while (column < x) {
	exes = exes + 'X';
	column++;
}
while (row < x)
{
	console.log(exes);
	row++;
}
