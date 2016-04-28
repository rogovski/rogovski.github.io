---
layout: post
title:  "Python Argparse lib"
date:   2016-04-28 13:14:00 -0500
categories: python
description: "links and sources"
---


[doc page for python 3](https://docs.python.org/3/library/argparse.html)

[doc page for python 2](https://docs.python.org/2.7/library/argparse.html)

```python
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()

print(args.accumulate(args.integers))
```