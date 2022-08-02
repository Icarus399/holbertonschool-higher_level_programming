#!/usr/bin/node
// Script that prints the first args passed to it

const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
