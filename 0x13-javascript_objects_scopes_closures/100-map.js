#!/usr/bin/node
const list = require('./100-data.js').list;
const result = list.map((curr, id) => curr * id);
console.log(list);
console.log(result);
