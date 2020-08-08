#!/usr/bin/node
let num = 0;
exports.logMe = function (item) {
  console.log('%d: %s', num, item);
  num++;
};
