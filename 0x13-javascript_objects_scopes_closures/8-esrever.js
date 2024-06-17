#!/usr/bin/node
/* returns reversed version of a list */
/* don't use built in method */

exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const aux = list[len];
    list[len] = list[i];
    list[i] = aux;
    len--;
    i++;
  }
  return list;
};
