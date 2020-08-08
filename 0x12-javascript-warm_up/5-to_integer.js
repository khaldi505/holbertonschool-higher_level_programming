#!/usr/bin/node
const string = process.argv;
const type = parseInt(string[2], 10);

if (!string[2] || isNaN(type)) { console.log('Not a number'); }

if (string[2] && !isNaN(type)) {
  console.log('My number: ' + parseInt(string[2], 10));
}
