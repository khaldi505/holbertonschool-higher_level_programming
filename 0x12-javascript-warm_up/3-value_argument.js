#!/usr/bin/node
const string = process.argv;

if (string[2]) { console.log(string[2]); } else {
  console.log('No argument');
}
