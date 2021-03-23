#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  for (let x = 0; x < len; x++, len--) {
    const temp = list[x];
    list[x] = list[len];
    list[len] = temp;
  }
  return list;
};
