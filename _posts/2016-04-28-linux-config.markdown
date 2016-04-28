---
layout: post
title:  "Linux Configuration"
date:   2016-04-28 13:14:00 -0500
categories: linux
description: "links and sources"
---


[SO answer](http://stackoverflow.com/a/1024121)

1. Generally system/global config is stored somewhere under /etc.
2. User-specific config is stored in the user's home directory, often as a hidden file, sometimes as a hidden directory containing non-hidden files (and possibly more subdirectories).

Generally speaking, command line options will override environment variables which will override user defaults which will override system defaults.