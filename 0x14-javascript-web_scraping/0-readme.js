#!/usr/bin/node
/* reads and prints the contents of a file */
const reader = require('fs');
reader.readFile(process.argv[2], 'utf-8', function (error, content) {
  console.log(error || content);
}
);
