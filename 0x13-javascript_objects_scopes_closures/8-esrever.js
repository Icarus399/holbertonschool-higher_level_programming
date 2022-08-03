#!/usr/bin/node
// Write a function that returns the reversed version of a list

exports.esrever = function (list) {
  const reverlist = [];
  let i = list.length - 1;
  while (i >= 0) {
    reverlist.push(list[i]);
    i--;
  }
  return (reverlist);
};
