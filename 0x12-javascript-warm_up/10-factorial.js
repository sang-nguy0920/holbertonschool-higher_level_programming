#!/usr/bin/node

function facts (x) {
  if (x > 0) {
    return (x * facts(x - 1));
  } else {
    return 1;
  }
}

const res = parseInt(process.argv[2]);
console.log(facts(res));
