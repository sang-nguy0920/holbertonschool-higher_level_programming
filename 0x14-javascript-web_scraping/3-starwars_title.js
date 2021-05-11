#!/usr/bin/node

const request = require('request');

const host = 'https://swapi-api.hbtn.io/api/films/'.concat('', process.argv[2]);

request(host, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
