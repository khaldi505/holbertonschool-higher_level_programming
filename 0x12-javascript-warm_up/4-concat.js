#!/usr/bin/node
const string = process.argv;

if (string[2] && string[3]) { console.log(string[2] + ' is ' + string[3]); } else if (string[2] && !string[3]) { console.log(string[2] + ' is ' + 'undefined'); } else { console.log('undefined is undefined'); }
