#!/usr/bin/node
/* returns the numbor of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let i = 0;
  let count = 0;
  while (i < len) {
    if (list[i] === searchElement) {
      count++;
    }
    i++;
  }
  return (count);
};

/* exports.nbOccurences = nb0ccurences; */
