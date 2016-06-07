---
layout: post
title:  "Node Streams"
date:   2016-06-07 13:14:00 -0500
categories: javascript
description: "links and sources"
---

```javascript

var Readable = require('stream').Readable,
    Writable = require('stream').Writable,
    Transform = require('stream').Transform,
    util = require('util');

// we can almost think of a READABLE stream as a 'lazy' loop that gets iterated by the caller
// each call to read is an explicit instruction to iterate the loop
var ReadStream = function() {
  Readable.call(this, {objectMode: true});
  this.currChar = 97; // 'a'
};
util.inherits(ReadStream, Readable);


ReadStream.prototype._read = function() {
  // stream end condition
  if (this.currChar > 'z'.charCodeAt(0)) {
    this.push(null);
  }
  else {
      // one iteration of the underlying data character
      this.push(String.fromCharCode(this.currChar));
      this.currChar++;
  }

};


/**
 * //////////////////////////////////////////
 * // same as process.stdout. writes objects
 * //////////////////////////////////////////
 */

var WriteStream = function() {
  Writable.call(this, {objectMode: true});
};
util.inherits(WriteStream, Writable);


WriteStream.prototype._write = function(chunk, encoding, callback) {
  console.log(chunk);
  callback();
};



var TransformStream_ChunkByN = function(n) {
  Transform.call(this, {objectMode: true});

  if(n === void 0 || n === null || n === 0) {
    throw new Error('invalid buffer size');
  }

  this.chunkSize = n;
  this.localBuffer = [];
};
util.inherits(TransformStream_ChunkByN, Transform);

TransformStream_ChunkByN.prototype.flushBuffer = function() {
    this.push(this.localBuffer);
    this.localBuffer = [];
};

TransformStream_ChunkByN.prototype._transform = function(chunk, encoding, callback) {

  this.localBuffer.push(chunk);

  if(this.localBuffer.length === this.chunkSize) {
    this.flushBuffer();
  }

  callback();
};
```
