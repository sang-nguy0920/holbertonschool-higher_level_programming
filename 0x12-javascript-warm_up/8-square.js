#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  for (let x = 0; x < size; x++) {
    console.log(Array(size + 1).join('X'));
  }
}
