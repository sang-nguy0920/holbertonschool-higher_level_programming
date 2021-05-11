#!/usr/bin/node

const request = require('request');

const host = process.argv[2];

request(host, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  let occ = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        occ = occ + 1;
      }
    }
  }
  console.log(occ);
});
