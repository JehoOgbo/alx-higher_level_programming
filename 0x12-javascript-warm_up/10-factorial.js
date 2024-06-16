#!/usr/bin/node
/* prints the factorial of the given number */
/* use a function and do this recursively */
function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return (1);
  }
  return (num * factorial(num - 1));
}

const number = process.argv[2];
console.log(factorial(number));
