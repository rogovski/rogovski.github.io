---
layout: post
title:  "Probability Theory"
date:   2016-04-24 13:14:00 -0500
categories: mathematics statistics
description: "links and sources"
---


[cs229 probability review](http://cs229.stanford.edu/section/cs229-prob.pdf)

[Measurable Function](https://en.wikipedia.org/wiki/Measurable_function)

borel measurable function

<!--
    http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
    http://cs229.stanford.edu/section/cs229-prob.pdf
    https://en.wikipedia.org/wiki/Measurable_function
    https://en.wikipedia.org/wiki/Measure_(mathematics)
    https://en.wikipedia.org/wiki/Lebesgue_measure
    https://en.wikipedia.org/wiki/Sigma-algebra
    http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
    https://en.wikipedia.org/wiki/Mixture_model
-->
    <ul>
        <li>
            Sample Space $\Omega$: the SET of possible outcomes or observations.
            Note the 'type' of $\Omega$ - it is a set of uniterpreted items $SET_0$.
            elements (or observations) of this set are labeled $\omega \in \Omega$
        </li>
        <li>
            Event Space $\mathcal{F}$: the SET of events $A \in \mathcal{F}$ and $A \subseteq \Omega$.
            Note the 'type' of $\mathcal{F}$ - it is a set of sets (a set of subsets of $\Omega$) $SET_1$.
            The Event Space must have the following properties:
            <ol>
              <li>
                $\emptyset \in \mathcal{F}$ (the empty set is in $\mathcal{F}$)
              </li>
              <li>
                $A \in \mathcal{F} \Rightarrow \Omega \setminus A \in \mathcal{F}$
                (if $A$ is an event in $\mathcal{F}$ then the relative complement of $A$ with respect to $\Omega$ is also in $\mathcal{F}$)
              </li>
            </ol>
        </li>
        <li>
            Probability Measure $P : \mathcal{F} \to \Bbb{R}$: maps an event in the event space to a real number
        </li>

    </ul>