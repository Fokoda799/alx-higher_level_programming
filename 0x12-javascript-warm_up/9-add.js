#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const argA = process.argv[2];
const argB = process.argv[3];

if (isNaN(argA) || isNaN(argB)) {
  console.log('NaN');
} else {
  const a = parseInt(argA);
  const b = parseInt(argB);
  console.log(add(a, b));
}
