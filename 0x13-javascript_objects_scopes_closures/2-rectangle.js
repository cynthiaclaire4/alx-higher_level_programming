#!/usr/bin/node
// If w or h is equal to 0 or not a positive integer, create an empty object
module.exports = class Retangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
