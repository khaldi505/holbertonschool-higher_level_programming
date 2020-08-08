#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  const array = [];
  let s = 0;
  while ((len >= 0)) {
    array[s] = list[len];
    s++;
    len--;
  }
  return array;
};
