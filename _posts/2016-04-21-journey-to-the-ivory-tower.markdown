---
layout: post
title:  "Types: Journey to the Ivory Tower"
date:   2016-04-21 13:14:00 -0500
categories: mathematics cs
description: "How types can affect your daily programming experience"
---

*the following consists of snippets copied and pasted wikipedia entries. this content was not produced by me.*

in the begining there was mathematics

[def: function](https://en.wikipedia.org/wiki/Function_(mathematics))

function: black box analogy

functions vs subroutines

[def: expression](https://en.wikipedia.org/wiki/Expression_(computer_science))

An expression in a programming language is a combination of one or
more explicit values, constants, variables, operators, and functions
that the programming language interprets (according to its particular
rules of precedence and of association) and computes to produce ("to
return", in a stateful environment) another value. This process, as
for mathematical expressions, is called evaluation.

In simple settings, the resulting value is usually one of various
primitive types, such as numerical, string, and logical; in more
elaborate settings, it can be an arbitrary complex data type. In
functional programming, the resulting values are often functions or
expressions, which can themselves be further evaluated.

For example, 2+3 is an arithmetic and programming expression which
evaluates to 5. A variable is an expression because it denotes a value
in memory, so y+6 is an expression. An example of a relational
expression is 4≠4, which evaluates to false.[1][2]

In C and most C-derived languages, a call to a function with a void
return type is a valid expression, of type void.[3] Values of type
void cannot be used, so the value of such an expression is always
thrown away.

[def: Referential Transparency](https://en.wikipedia.org/wiki/Referential_transparency)

Referential transparency and referential opacity are properties of
parts of computer programs. An expression is said to be referentially
transparent if it can be replaced with its value without changing the
behavior of a program (in other words, yielding a program that has the
same effects and output on the same input). The opposite term is
referential opacity.

With referential transparency, no distinction is made nor difference
recognized between a reference to a thing and the corresponding thing
itself. Without referential transparency, such difference can be
easily made and utilized in programs.

While in mathematics all function applications are referentially
transparent, in programming this is not always the case.....

why?

[def: Side Effect](https://en.wikipedia.org/wiki/Side_effect_(computer_science))

In computer science, a function or expression is said to have a side
effect if it modifies some state or has an observable interaction with
calling functions or the outside world.

side effects - changes in state that do not depend on the function inputs

[def: Functional Programming](https://en.wikipedia.org/wiki/Functional_programming)


[def: Immutable Object](https://en.wikipedia.org/wiki/Immutable_object)
In object-oriented and functional programming, an immutable object
(unchangeable[1] object) is an object whose state cannot be modified
after it is created.[2] This is in contrast to a mutable object
(changeable object) , which can be modified after it is created. In
some cases, an object is considered immutable even if some internally
used attributes change but the object's state appears to be unchanging
from an external point of view. For example, an object that uses
memoization to cache the results of expensive computations could still
be considered an immutable object.

[def: Purely functional](https://en.wikipedia.org/wiki/Purely_functional)
In computing, an algorithm, data structure, or programming language is
called purely functional if they guarantee the (weak) equivalence of
call-by-name, call-by-value and call-by-need evaluation strategies.

[def: Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
Ad hoc polymorphism: when a function denotes different and potentially
heterogeneous implementations depending on a limited range of
individually specified types and combinations. Ad hoc polymorphism is
supported in many languages using function overloading.

Parametric polymorphism: when code is written without mention of any
specific type and thus can be used transparently with any number of
new types. In the object-oriented programming community, this is often
known as generics or generic programming. In the functional
programming community, this is often shortened to polymorphism.

Subtyping (also called subtype polymorphism or inclusion
polymorphism): when a name denotes instances of many different classes
related by some common superclass.[3] In the object-oriented
programming community, this is often simply referred to as
polymorphism.

The interaction between parametric polymorphism and subtyping leads to
the concepts of variance and bounded quantification.

[def: Natural Deduction](https://en.wikipedia.org/wiki/Natural_deduction)
-> Judgments and propositions
