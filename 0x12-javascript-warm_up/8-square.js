#!/usr/bin/node
// Script that prints a Square

const count = process.argv[2];
let i = 0;

if (parseInt(count)) {
  for (; i < count; i++) {
    console.log('X'.repeat(count));
  }
} else {
  console.log('Missing size');
}
