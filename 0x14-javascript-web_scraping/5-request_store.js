#!/usr/bin/node
/* get the content of a webpage and store it in a file */
/* the first argument is the URL to request */
/* the second arg is the file path to store the body response */
const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
