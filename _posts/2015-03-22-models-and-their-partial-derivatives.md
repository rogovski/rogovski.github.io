---
layout: post
title: Two Models and Their Partial Derivatives
---

While doing some Calculus homework the other day, I came across two exercises that I
found pretty interesting. The problems provided data in a tabular format as well as
a model (given as a function of x and y). Here is the first of the two:

| year | 2005  | 2006  | 2007  | 2008  | 2009  | 2010  |
| ---- | ----- | ----- | ----- | ----- | ----- | ----- |
| x    | 36.4  | 39.0  | 42.4  | 44.7  | 43.0  | 45.2  |
| y    | 15.3  | 16.6  | 17.4  | 17.5  | 17.0  | 17.3  |
| z    | 16.4  | 18.1  | 20.0  | 20.5  | 20.1  | 21.4  |

```r
x <- c(36.4,39.0,42.4,44.7,43.0,45.2)
y <- c(15.3,16.6,17.4,17.5,17.0,17.3)
z <- c(16.4,18.1,20.0,20.5,20.1,21.4)

d <- data.frame(x,y,z)

mdl <- lm(z ~ x + y, data = d)
```
