#!/usr/bin/node

const string = process.argv;
const type = parseInt(string[2], 10);

if (!string[2] || (isNaN(type))) { console.log('Missing number of occurrences'); } else if (string[2] && !(isNaN(type)) && string[2] > 0) {
  for (let x = 0; x !== type; x++) {
    console.log('C is fun');
  }
}
