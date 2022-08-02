#!/usr/bin/node
// Script that prints the first arg can be converted to an int

const num = process.argv[2];
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
