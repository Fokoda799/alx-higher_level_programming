#!/usr/bin/node

const { argv } = require('node:process');
let myVar;
if (argv.length === 2) {
  myVar = 'No argument';
} else if (argv.length === 3) {
  myVar = 'Argument found';
} else {
  myVar = 'Arguments found';
}
console.log(myVar);
