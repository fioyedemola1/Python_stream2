from functools import wraps
from typing import Optional,Any

def checks(item):
    def inner(func):
        @wraps(func)
        def wrapper(value:Optional[Any]=None,*args):
            if value == None:
                print(f'{func.__name__}, has no value')
                return 
            print('*' * 10)
            ans = func(value)
            if item != type(ans):
                print(ans, type(ans))
                print('Your answer is  incorrect')
                print('*' * 10)
                return
            else:
                print('Test passed')
            print('*' * 10)
        return wrapper
    return inner
