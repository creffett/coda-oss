# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_mt')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_mt')
    _mt = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mt', [dirname(__file__)])
        except ImportError:
            import _mt
            return _mt
        try:
            _mod = imp.load_module('_mt', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _mt = swig_import_helper()
    del swig_import_helper
else:
    import _mt
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

import coda.coda_except
import coda.coda_sys
class Runnable(_object):
    """Proxy of C++ sys::Runnable class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Runnable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Runnable, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _mt.delete_Runnable
    __del__ = lambda self: None

    def run(self):
        """run(Runnable self)"""
        return _mt.Runnable_run(self)

Runnable_swigregister = _mt.Runnable_swigregister
Runnable_swigregister(Runnable)

class ThreadPlanner(_object):
    """Proxy of C++ mt::ThreadPlanner class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ThreadPlanner, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ThreadPlanner, name)
    __repr__ = _swig_repr

    def __init__(self, numElements, numThreads):
        """__init__(mt::ThreadPlanner self, size_t numElements, size_t numThreads) -> ThreadPlanner"""
        this = _mt.new_ThreadPlanner(numElements, numThreads)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def getNumElementsPerThread(self):
        """getNumElementsPerThread(ThreadPlanner self) -> size_t"""
        return _mt.ThreadPlanner_getNumElementsPerThread(self)


    def getNumThreadsThatWillBeUsed(self):
        """getNumThreadsThatWillBeUsed(ThreadPlanner self) -> size_t"""
        return _mt.ThreadPlanner_getNumThreadsThatWillBeUsed(self)


    def getThreadInfo(self, threadNum):
        """getThreadInfo(ThreadPlanner self, size_t threadNum) -> PyObject *"""
        return _mt.ThreadPlanner_getThreadInfo(self, threadNum)

    __swig_destroy__ = _mt.delete_ThreadPlanner
    __del__ = lambda self: None
ThreadPlanner_swigregister = _mt.ThreadPlanner_swigregister
ThreadPlanner_swigregister(ThreadPlanner)

class ThreadGroup(_object):
    """Proxy of C++ mt::ThreadGroup class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ThreadGroup, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ThreadGroup, name)
    __repr__ = _swig_repr

    def __init__(self, pinToCPU=False):
        """
        __init__(mt::ThreadGroup self, bool pinToCPU=False) -> ThreadGroup
        __init__(mt::ThreadGroup self) -> ThreadGroup
        """
        this = _mt.new_ThreadGroup(pinToCPU)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mt.delete_ThreadGroup
    __del__ = lambda self: None

    def joinAll(self):
        """joinAll(ThreadGroup self)"""
        return _mt.ThreadGroup_joinAll(self)


    def createThread(self, runnable):
        """createThread(ThreadGroup self, PyObject * runnable)"""
        return _mt.ThreadGroup_createThread(self, runnable)

ThreadGroup_swigregister = _mt.ThreadGroup_swigregister
ThreadGroup_swigregister(ThreadGroup)

# This file is compatible with both classic and new-style classes.


