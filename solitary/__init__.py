"""
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
"""

# Overview

Solitary is a module which aims to make it easy to have classes behave
like singletons - in that you only ever get one active instance of the
class at any one time.

This module allows you to implement this through decorator form, meaning its
trivial to implement and does not require you to manage the __new__ and __init__
relationships for simple singleton-like behaviour.

Here is an example of use:

```python
import solitary

# -- Define our class, but wrap the class in our
# -- singleton declaration
@solitary.singleton
class Foo(object):
    pass


# -- Now we can instance this class multiple times, but
# - they will all be the same
a = Foo()
b = Foo()

print(a==b)
# True
```

The classes being decorated can contain init arguments, though only the first instance
ever has those arguments utilised, as shown in this example:

```python
import solitary

# -- Define our class, but wrap the class in our
# -- singleton declaration
@solitary.singleton
class Foo(object):
    def __init__(self, x):
        self.value = x


# -- Now we can instance this class multiple times, but
# - they will all be the same
a = Foo(5)
b = Foo(2)

print(b.value)
# 5
```

In situations where you need to clear any cached singletons, and need to create
a new instance you can do so using the flush function as shown here:

```python
import solitary

# -- Define our class, but wrap the class in our
# -- singleton declaration
@solitary.singleton
class Foo(object):
    pass


# -- Create an instance of the class
a = Foo()

# -- Flush the cache
solitary.flush()

# -- Instance another Foo
b = Foo()

# -- We now have two instances, but they are unique
print(a==b)
# False
```

Much in the same vein, calling flush with no arguments will flush ALL
singleton declarations. You can flush only a specific class by passing
it as an argument.

```python
solitary.flush(Foo)
```

# Compatibility

Crab has been tested on __Windows__ using __Maya 2019__ and __Maya 2020__.


# Contribute

If you would like to contribute thoughts, ideas, fixes or features please get in touch! mike@twisted.space

"""
from .core import flush
from .core import singleton

__version__ = '1.0.1'
