from functools import partial
from functools import wraps


class _NoValue(object):
    """Represents an unset value. Used to differeniate between an explicit
    ``None`` and an unset value.
    """
    pass

NoValue = _NoValue()


class GenerativeBase(object):
    def _generate(self):
        s = self.__class__.__new__(self.__class__)
        s.__dict__ = self.__dict__.copy()
        return s


def _generative(func):
    @wraps(func)
    def decorator(self, *args, **kw):
        self = self._generate()
        func(self, *args, **kw)
        return self
    return decorator


class ChainTest2(GenerativeBase):

    def __init__(self,  list=[]):

        self.func_lookup = {}
        self.func_lookup['_in'] = '_in_'
        self.func_lookup['_out'] = '_out_'
        self.func_lookup['v'] = '_v_'

        self.callmap = {}
        self._value =  list
        self.callmap['_in'] = partial(self._in_)
        self.callmap['_out'] = partial(self._out_)
        self.callmap['v'] = partial(self._v_)

        module = ChainTest2

        self._list = list

    @_generative
    def _in_(self, *args):
        self._list.append(args[0])
        print('_in: ' + repr(args))
        return self

    @_generative
    def _out_(self, *args):
        self._list.append(args[0])
        print('_out: ' + repr(args))
        return self

    @_generative
    def _v_(self, *args):
        self._list.append(args[0])
        print('vertex: ' + repr(args))
        return self

    def run(self):
        """Return current value of the chain operations."""
        return self(self._value)

    # @classmethod
    # def get_method(cls, name):
    #     """Return valid 'module' method."""
    #
    #     print("Get Method - " + repr(name))
    #
    #     method = getattr(cls, name, None)
    #
    #     if not callable(method):
    #         raise BaseException
    #
    #     return method

    def __getattr__(self, name, *args):
        print("Looking for " + name)
        print(args)
        func = self.callmap[name]
        return func

    #     return ChainWrapper2(self._value, self.get_method(func))
    #
    def __call__(self, value):
        print("Call:Value = " + repr(value))
        if isinstance(self._value, ChainWrapper2):
            value = self._value
        return value


class ChainWrapper2(object):
    """Wrap 'Chain' method call within a 'ChainWrapper' context."""

    def __init__(self, value, method):
        print("Making new Wrapper")
        self._value = value
        self.method = method
        self.args = ()
        self.kargs = {}

    def _generate(self):
        """Generate a copy of this instance."""
        print('In ChainWrapper _Generate')
        new = self.__class__.__new__(self.__class__)
        new.__dict__ = self.__dict__.copy()
        return new

    def unwrap(self, value=NoValue):
        """Execute 'method' with '_value', 'args', and 'kargs'. If '_value' is
        an instance of 'ChainWrapper', then unwrap it before calling 'method'.
        """
        # Generate a copy of ourself so that we don't modify the chain wrapper
        # _value directly. This way if we are late passing a value, we don't
        # "freeze" the chain wrapper value when a value is first passed.
        # Otherwise, we'd locked the chain wrapper value permanently and not be
        # able to reuse it.
        wrapper = self._generate()

        print('UnWrapping')

        if isinstance(wrapper._value, ChainWrapper2):
            wrapper._value = wrapper._value.unwrap(value)
        elif not isinstance(value, ChainWrapper2) and value is not NoValue:
            # Override wrapper's initial value.
            wrapper._value = value

        if wrapper._valueis is not NoValue:
            value = wrapper._value

        return wrapper.method(value, *wrapper.args, **wrapper.kargs)

    def __call__(self, *args, **kargs):
        """Invoke the 'method' with 'value' as the first argument and return a
        new 'Chain' object with the return value.
        """
        print("Wrapper-Call:Value = " + str(args))
        self.args = args
        self.kargs = kargs
        return ChainTest2(self)


if __name__ == "__main__":
    c = ChainTest2()
    #c.v(1)._in('Test')._out('Test2')._in('Test3')
    c.v(1)._in_('Test')._out_('Test2')._in_('Test3')
    c.run()

    #c("Call")
