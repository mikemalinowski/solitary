import types
import weakref


# -- We store singleton declarations in this dictionary
# -- as weakref's. This allows them to be garbage collected
_WEAK_WRAPPED_CLASSES = dict()


# --------------------------------------------------------------------------------------------------
def flush(cls=None):
    """
    Clears the cache of singleton delcared classes.

    :param cls: If given only this class will be cleared from the singleton
        cache. If None then all classes will be cleared.
    :return:
    """
    global _WEAK_WRAPPED_CLASSES

    # -- If we're given a specific class to flush, only flush
    # -- that one class
    if cls:
        if cls in _WEAK_WRAPPED_CLASSES:
            _WEAK_WRAPPED_CLASSES.pop(cls)
        return

    # -- Flush everything!
    _WEAK_WRAPPED_CLASSES = dict()


# --------------------------------------------------------------------------------------------------
def singleton(cls):
    """
    Decorator for delcaring on classes. This makes the class act like a singleton in that
    if the class has already been instantiated then the existing instance will be returned.

    The aim of this decorator is to make it simple to create basic simpletons without having
    to implement the __new__ method etc.

    :param cls:  The class to be declared as a singleton
    :type cls: class

    :return: func
    """
    # -- We only allow the decorating of classes, so we need
    # -- to raise an exception if this rule is broken.
    if not isinstance(object, (type, types.ClassType)):
        raise Exception(
            'Attempt to wrap a non-class object as a solitary (singleton) class.'
        )

    # -- Declare our lookup argument as global
    global _WEAK_WRAPPED_CLASSES

    def _wrapper(*args, **kwargs):

        # -- TODO: Sould we use a weakref?
        # -- If there is a class instance for this already, and its valid
        # -- the we should use it
        if cls in _WEAK_WRAPPED_CLASSES:
            if _WEAK_WRAPPED_CLASSES[cls]():
                return _WEAK_WRAPPED_CLASSES[cls]()

        # -- No class was available, so we instance a new one
        inst = cls(*args, **kwargs)

        # -- Now we have an instance we store it to allow the next
        # -- instance attempt to utilise it
        _WEAK_WRAPPED_CLASSES[cls] = weakref.ref(inst)

        # -- Return our instance
        return inst
    return _wrapper
