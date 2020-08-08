#!/usr/bin/node
function factorial (fac) {
  if (parseInt(fac, 10) === 1) { console.log('NaN'); } else if (parseInt(fac, 10) !== 1) {
    let test = 1;
    for (let hbach = 1; hbach <= fac; hbach++) {
      test *= hbach;
    }
    console.log(test);
  }
}
factorial(process.argv[2]);
