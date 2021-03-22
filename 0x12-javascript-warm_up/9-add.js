#!/usr/bin/node

function add (a, b) {
    const sumation = a + b;
    console.log(sumation);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
add(a, b);
