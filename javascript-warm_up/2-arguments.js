#!/usr/bin/node
//if there is no 3rd argument
if (process.argv.length === 2) {
    console.log('No argument')
}
//if there is 3 or more arguments then there is input
else if (process.argv.length === 3) {
    console.log('Argument found')
}
else {
    console.log('Arguments found')
}
