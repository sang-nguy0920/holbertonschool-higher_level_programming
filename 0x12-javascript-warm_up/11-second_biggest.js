#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const argv = process.argv.slice(2);
  console.log(argv.sort()[argv.length - 2]);
}
