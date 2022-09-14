#!/usr/bin/node
// Write a script that reads and prints the content of a file.

const fs = require('fs');
const file = process.argv[2];
fs.readFileSync(file, 'utf8');
fs.readFile(file, function (err, data) {
  if (err) return console.error(err);
  console.log(data.toString());
});
