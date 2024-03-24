#!/usr/bin/node
const { argv } = require("node:process");
let myVar = argv[2];
try {
    if (myVar === null){
        myVar = "No argument";
    }
} catch () {

console.log(myVar);
