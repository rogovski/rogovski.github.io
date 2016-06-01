---
layout: post
title:  "Python Threading"
date:   2016-06-01 13:14:00 -0500
categories: python
description: "links and sources"
---


```python
import threading
import time

# https://docs.python.org/2/library/threading.html
# https://docs.python.org/2/library/threading.html#thread-objects
# http://www.tutorialspoint.com/python/python_multithreading.htm
# http://effbot.org/zone/thread-synchronization.htm

def worker():
    print 'working'
    return

# constructing a new thread (no args)
# t = threading.Thread(target=worker)

def workerArgs(a0, a1):
    print 'working %s %s' % (a0, a1)
    return

# constructing a new thread (2 args)
# t = threading.Thread(target=workerArgs, args=('ok', 'cool'))

def sleeper():
    print 'working'
    time.sleep(10)
    return

# this will start the sleeper thread
# and poll it
def testIsAliveOnSleeper():
    t = threading.Thread(target=sleeper);
    t.start();
    time.sleep(1); print t.isAlive();time.sleep(1); print t.isAlive();
    time.sleep(1); print t.isAlive();time.sleep(1); print t.isAlive();
    time.sleep(1); print t.isAlive();time.sleep(1); print t.isAlive();
    time.sleep(1); print t.isAlive();time.sleep(1); print t.isAlive();
    time.sleep(1); print t.isAlive();time.sleep(1); print t.isAlive();
    time.sleep(1); print t.isAlive();time.sleep(1); print t.isAlive();
    time.sleep(1); print t.isAlive();time.sleep(1); print t.isAlive();
    time.sleep(1); print t.isAlive();time.sleep(1); print t.isAlive();

# methods defined on thread
# t.daemon    t.ident     t.isDaemon  t.join      t.run       t.setName
# t.getName   t.isAlive   t.is_alive  t.name      t.setDaemon t.start


# A thread can be flagged as a “daemon thread”.
# The significance of this flag is that the entire
# Python program exits when only daemon threads are left.
# The initial value is inherited from the creating thread.
# The flag can be set through the daemon property.

# Note Daemon threads are abruptly stopped at shutdown.
# Their resources (such as open files, database transactions, etc.)
# may not be released properly. If you want your threads to stop
# gracefully, make them non-daemonic and use a suitable signalling
# mechanism such as an Event.

# according to effbot article
###################################################################
# Atomic Operations
#
# The simplest way to synchronize access to shared variables or other
# resources is to rely on atomic operations in the interpreter.
# An atomic operation is an operation that is carried out in a single
# execution step, without any chance that another thread gets control.
#
# In general, this approach only works if the shared resource consists
# of a single instance of a core data type, such as a string variable,
# a number, or a list or dictionary. Here are some thread-safe
# operations:
#
# * reading or replacing a single instance attribute
# * reading or replacing a single global variable
# * fetching an item from a list
# * modifying a list in place (e.g. adding an item using append)
# * fetching an item from a dictionary
# * modifying a dictionary in place (e.g. adding an item, or calling
#   the clear method)
#
# Note that as mentioned earlier, operations that read a variable or
# attribute, modifies it, and then writes it back are not thread-safe.
# Another thread may update the variable after it’s been read by the
# current thread, but before it’s been updated.
#
# Also note that Python code may be executed when objects are
# destroyed, so even seemingly simple operations may cause other
# threads to run, and may thus cause conflicts. When in doubt, use
# explicit locks.
```
