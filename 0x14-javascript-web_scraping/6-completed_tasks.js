#!/usr/bin/node

const request = require('request');
const host = process.argv[2];

request(host, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }

  const dict = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
  };

  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      dict[task.userId]++;
    }
  }

  for (const key in dict) {
    const value = dict[key];

    if (value === 0) {
      delete dict[key];
    }
  }
  console.log(dict);
});
