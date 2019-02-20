# sly/ast.py
import sys

class AST(object):
    
    @classmethod
    def __init_subclass__(cls, **kwargs):
        mod = sys.modules[cls.__module__]
        if not hasattr(cls, '__annotations__'):
            return

        hints = list(cls.__annotations__.items())

        def __init__(self, *args, **kwargs):
            if len(hints) != len(args):
                raise TypeError('Expected {} arguments'.format(len(hints)))
            for arg, (name, val) in zip(args, hints):
                if isinstance(val, str):
                    val = getattr(mod, val)
                if not isinstance(arg, val):
                    raise TypeError('{} argument must be {}'.format(name, val))
                setattr(self, name, arg)

        cls.__init__ = __init__

