#!/usr/bin/node

if ((!process.argv[2] || !process.argv[3])) {
  console.log('0');
} else {
  let array = [];
  let counter = 2;
  while ((counter !== process.argv.length)) { array.push(parseInt(process.argv[counter])); counter++; }
  array = array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
