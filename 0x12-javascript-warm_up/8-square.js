#!/usr/bin/node
const firstarg = process.argv[2];

if (!process.argv[2] || isNaN(parseInt(process.argv[2], 10))) { console.log('Missing size'); }

for (let x = 0; x < firstarg; x++) {
  for (let y = 0; y < firstarg; y++) {
    process.stdout.write('X');
  }
  process.stdout.write('\n');
}
