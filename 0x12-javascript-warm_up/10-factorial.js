#!/usr/bin/node
const arg = process.argv[2];
function factorail (num) {
  if (num === 1) {
    return 1;
  }
  return num * factorail(num - 1);
}
if (isNaN(arg)) {
  console.log(1);
} else {
  const num = parseInt(arg);
  console.log(factorail(num));
}
