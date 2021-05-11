#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const host = process.argv[2];
const file = process.argv[3];

request(host, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(file, body, (err, data) => {
    if (err) {
      console.error(err);
    }
  });
});
