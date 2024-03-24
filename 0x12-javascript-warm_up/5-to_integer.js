#!/usr/bin/node
const arg = process.argv[2];
let myVar;
if (isNaN(arg)) {
  myVar = 'Not a number';
} else {
  myVar = parseInt(arg);
}
console.log(myVar);
