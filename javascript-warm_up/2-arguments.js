#!/usr/bin/node
// if there is no 3rd argument
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
    // if there is 3 or more arguments then there is input
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
