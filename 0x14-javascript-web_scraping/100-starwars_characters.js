#!/usr/bin/node
/* Prints all characters of a star wars movie */
const request = require('request');
const movieId = process.argv[2];
let url = 'https://swapi-api.alx-tools.com/api/films/';
url = url + movieId;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const movieDetails = JSON.parse(body).characters;
  for (let i = 0; i < movieDetails.length; i++) {
    request(movieDetails[i], function (error, response, body) {
      if (error) {
        return;
      }
      const charDetails = JSON.parse(body).name;
      console.log(charDetails);
    });
  }
});
