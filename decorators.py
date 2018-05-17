# -*- coding: utf-8 -*-

"""
⚡⚡⚡ Welcome to RHV QE Lightning Talk! ⚡⚡⚡
Topic: Define Function Decorators with functools.wraps

How to execute this demo:
- Open IPython console in this directory.
- from IPython.lib.demo import Demo
- demo = Demo('decorators.py')
- Call demo() to start
- Call demo() everytime you want to continue
"""

# <demo> ---stop---

"""
⚡ What is decorator?
A decorator is a function that takes a function object as its argument, 
and returns a function object, 
and in the process, makes necessary modifications to the input function, 
possibly enhancing it. 

The result of the wrapping?

   1. Adds functionality of the function.
   2. Modifies the behavior of the function.
"""

# <demo> ---stop---

"""
⚡ A little bit of theory about functions:
- Functions are objects like every other
- They can be assigned to variables and passed around
- Functions can accept functions as input and also return them
"""

print('test')
x = 17

# <demo> ---stop---
