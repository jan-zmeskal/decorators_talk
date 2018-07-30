# -*- coding: utf-8 -*-


import functools
import time


from IPython import embed
from welcome import welcome
from random import randint























welcome()
embed()
"""
⚡ What is decorator?
A decorator is a function that takes a function object as its argument,
and returns a function object,
and in the process, makes necessary modifications to the input function,
possibly enhancing it.
"""

"""
⚡ A little bit of theory about functions:
- Functions are objects like every other
- They can be assigned to variables and passed around
- Let's inspect some function:
    __repr__()
    __name__
    __doc__
    __call__()
"""


def hello():
    """Prints words of wisdom."""
    print('Hello, world of functions!')


embed()
"""
⚡ Functions can accept functions as input and also return them
"""


def caller(func):
    """Accepts a function and calls it for you, lazy programmer!"""
    print('I am gonna call function "{}" for you!'.format(func.__name__))
    func.__call__()


def useless_function_factory(name):
    """Returns a function that prints your name. Don't ask me why."""
    def name_printer():
        print("All hail to magnificient {}!".format(name))
    return name_printer


embed()


"""
⚡ So what actually is decorator once once more?
Function that:
    - Takes function object as an arguemnt
    - Enriches it somehow
    - Returns function object again
"""


def poor_function():
    print('😢')


def enricher(input_function):
    def output_function():
        print("$$$ on the entry!")
        input_function()
        print("$$$ on the exit!")
    return output_function


embed()


"""
⚡ How do we apply decorator properly?
Let's use python syntatic sugar!
@ is an annotation telling python that a decorator must be applied.
"""


@enricher
def very_poor_function():
    print('😢😢😢')


embed()


"""
⚡ Let's do some more advanced stuff - timer!
"""


def timer(func):
    """Decorator monitoring how much time does a func need to execute."""
    def wrapper(*args, **kwargs):
        time_at_start = time.time()
        func(*args, **kwargs)
        time_at_end = time.time() - time_at_start
        print('⏰ {} took {} to execute'.format(func.__name__, time_at_end))
    return wrapper


@timer
def busybody(iterations):
    """Does a random calculation per iteration."""
    for _ in range(iterations):
        a = randint(1, 100)
        b = randint(1, 200)
        c = a + b
        print('{} + {} = {}'.format(a, b, c))


embed()
"""
⚡ Okay, that's all nice, but what about functools.wraps?
- Problem: We are just calling wrapper functions defined inside decorators
- This breakes introspection!
- Solution: functools.wraps copies metadata to the wrapper function
"""


def wait_before_start(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(3)
        func(*args, **kwargs)
    return wrapper


@wait_before_start
def goodbye():
    """One last emoji for you."""
    print('🐍')


embed()
"""
⚡ What are decorators good for?
- Few examples from CFME QE framework:
    - Blocking test cases based on blockers
    - Labeling test cases with tiers
    - Assigning provides to test cases
    - Adding metadata to test cases
    - Choosing implementation for a test case - admin UI, self-service, REST
"""
