"""
Decorators Definition
"""

#  Decorators are a very powerful and useful tool
#
# ▪ It allows programmers to modify the behavior of a function or a class
#
# ▪ Decorators allow us to wrap another function in order to extend the behavior of the
# wrapped function

"""
Creating Decorators
"""


# In the example below we create a decorator function that converts a sentence to upper case

def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


"""
Using Decorators
"""


# ▪ Our decorator function takes a function as an argument, so
# let us define a function and pass it to our decorator
#
# ▪ We learned earlier that we could assign a function to
# a variable
#
# ▪ We'll use that trick to call our decorator function

def say_hi():
    return 'hello there'


# decorate = uppercase_decorator(say_hi)
# decorate()

"""
Decorators and "@"
"""


# ▪ However, Python provides a much easier way for us to
# apply decorators
#
# ▪ We simply use the @ symbol before the function we would
# like to decorate

@uppercase
def say_hi():
    return 'hello there'


print(say_hi())  # HELLO THERE

"""
functools.wraps() 
"""

# ▪ In the given example, if we try to call the name of the
# wrapped function the result is "wrapper", and its docstring
# is lost

@uppercase
def say_hi():
    """Saying Hi"""
    return "hello there"


print(say_hi.__name__)  # wrapper
print(say_hi.__doc__)  # None


# ▪ To solve this problem, we use a decorator factory as a function
# decorator when defining a wrapper function

from functools import wraps

def uppercase(function):
    @wraps(function)
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result
    return wrapper
