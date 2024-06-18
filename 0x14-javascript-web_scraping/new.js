#!/usr/bin/node
/* displays the status of a GET request */
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error === null) {
    console.log('code:', response.statusCode);
  }
  console.log('body:', body);
}
);
