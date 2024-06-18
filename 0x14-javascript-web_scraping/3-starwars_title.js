#!/usr/bin/node
/* displays the status of a GET request */
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
  console.log(error || JSON.parse(body).title);
}
);
