#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  if ((x < 0)) { return; }
  while ((x !== 0)) {
    theFunction();
    x--;
  }
};
