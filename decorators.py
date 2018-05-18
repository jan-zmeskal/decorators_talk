# -*- coding: utf-8 -*-


from IPython import embed

"""
⚡⚡⚡ Welcome to RHV QE Lightning Talk! ⚡⚡⚡
Topic: Define Function Decorators with functools.wraps

⚡ What is decorator?
A decorator is a function that takes a function object as its argument,
and returns a function object,
and in the process, makes necessary modifications to the input function,
possibly enhancing it.

The result of the wrapping?

   1. Adds functionality of the function.
   2. Modifies the behavior of the function.
"""

"""
⚡ A little bit of theory about functions:
- Functions are objects like every other
- They can be assigned to variables and passed around
- Let's inspect some function: __repr__(), __name__ and __call__()
"""


def hello():
    """Prints words of wisdom."""
    print('Hello, world of functions!')


# embed()
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


# embed()


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


# embed()


"""
⚡ How do we apply decorator properly?
Let's use python syntatic sugar!
@ is an annotation telling python that a decorator must be applied.
"""

@enricher
def very_poor_function():
    print('😢😢😢')


embed()
