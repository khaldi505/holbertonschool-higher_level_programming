#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  let occ = 0;
  while ((list[x] < list.length)) {
    if ((searchElement === list[x])) { occ++; }
    x++;
  }
  return occ;
};
