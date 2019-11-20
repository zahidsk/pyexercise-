Foo = type('Foo',(),{})  # define class`
x = Foo()
print(x)

class Foo2:
    pass

x2 = Foo2()
print(x2)

print("===========================")
# 1.basic decorators
# 2.arguments
# 3.return from decorators

import functools


def twice(f):
    @functools.wraps(f)
    def wrapper(name):
        print("bfore function ...", f.__name__)
        ret = f(name)
        print("After function ...", f)
        return ret
    return wrapper


@twice
def display(name):
    print("Hi I am decorator..runby ..", name)
    return f'GM ..{name}'


p = display('sk')
print(p)
print(display.__name__)
