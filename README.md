
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

Crab has been tested on __Windows__ using under Python 2.7 and Python 3.7


# Contribute

If you would like to contribute thoughts, ideas, fixes or features please get in touch! mike@twisted.space
