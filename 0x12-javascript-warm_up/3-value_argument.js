#!/usr/bin/node
const arg = process.argv[2];
let myVar;
if (arg === undefined) {
  myVar = 'No argument';
} else {
  myVar = arg;
}
console.log(myVar);
