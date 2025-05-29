#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) return console.error(error);

  const film = JSON.parse(body);
  const characters = film.characters;

  // Fetch each character in order
  const fetchCharacters = (index) => {
    if (index === characters.length) return;
    request(characters[index], (err, res, data) => {
      if (err) return console.error(err);
      const character = JSON.parse(data);
      console.log(character.name);
      fetchCharacters(index + 1);
    });
  };

  fetchCharacters(0);
});
