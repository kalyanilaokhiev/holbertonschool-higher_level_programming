#!/usr/bin/node
const x = parseInt(process.argv[2]);

let i = 0;

if (Number.isInteger(x)) {
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
} else {
  console.log('Missing size');
}
