# Assign

---------

`assign` is a black magic module for supporting `obj.__assign__`:

### How to use it:

#### 1. magic patch

Suppose that there is a `test.py`

```python

a = 1


class T():
    def __assign__(self, v):
        print('called with %s' % v)


b = T()
c = b

```
It just works as:

```python
Python 3.6.0 (default, Mar  6 2017, 15:44:48)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import magic
>>> import test
called with c

```

#### 2. manually patch

```
from assign.patch import patch_module
import test

patch_module(test)

```

### Install

just:

`pip install assign`

### Notes

* Tested with `Py2.7` and `Py3.6`

### Known Issues

* 1. Won't work under `REPL`
* 2. May slow import operation.
* 3. May failed when patch some modules like `os` and `sys`