---
layout: post
title: Extracting Schemas from Unstructured Data Using Naive Bayes
---

### About the Title

I don't like the word 'Unstructured Data'.
There seem to be very few cases where data *is* structured.
Here are some examples of what i would considered

- Code that doesn't compile is unstructured data.
- The Well Formed CSV document pulled from Po Dunk's FTP server on a nightly basis is unstructured data.
- That municipality whose ancient (yet w3c complient) website we scrape is unstructured data.

There are countless contexts where this phrase is an adequate description,
but is, arguably, a misnomer. So I'm fixing the following as my definition:

> Unstructured Data (or unstructured information) refers to information that either does not
> have a pre-defined data model or is not organized in a pre-defined manner. Unstructured
> information is typically text-heavy, but may contain data such as dates, numbers, and facts
> as well. [+](http://en.wikipedia.org/wiki/Unstructured_data)

This definition suggests that we focus on the *source* of the data and ask what guarantees it provides.

### TODO

- [ ] describe the problem
  - [ ] csv files
  - [ ] rant
- [ ] naive bayes
  - [ ] attempt explaination
  - [ ] use for stuff