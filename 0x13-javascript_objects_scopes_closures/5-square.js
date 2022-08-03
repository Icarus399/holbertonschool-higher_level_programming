#!/usr/bin/node
// Write a class Square that defines a rectangle

const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
