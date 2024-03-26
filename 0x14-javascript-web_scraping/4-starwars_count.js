#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];
const AntillesID = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(URL, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
  } else {
    if (response.statusCode === 200) {
      const movieINFO = JSON.parse(body).results;
      const AntillesFilms = movieINFO.filter(film => film.characters.includes(AntillesID));
      console.log(`${AntillesFilms.length}`);
    } else {
      console.error('Error occurred:', error);
    }
  }
});
