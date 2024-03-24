#!/usr/bin/node

const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let squareSize = parseInt(size);
  if (squareSize <= 0) {
    squareSize = 0;
  } else {
    for (let i = 0; i < squareSize; i++) {
      let row = '';
      for (let j = 0; j < squareSize; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
