# -*- coding: utf-8 -*-
import time, functools
def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin call:')
                print('%s %s:' % (text, func.__name__))
                f=func(*args, **kw)
                print('end call')
                return f
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args,**kw):
            print('begin call: %s' % text.__name__)
            f=text(*args,**kw)
            print('end call')
            return f
        return wrapper


@log 
def a(x,y):
    return x+y


@log('bb')
def b(x,y):
    return x*y


print(b(5,6))
print(a(11,12))
