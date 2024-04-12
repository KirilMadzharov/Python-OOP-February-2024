"""
Accepting Arguments
"""


# *args

# Sometimes, we might need to define a decorator
# that accepts arguments
#
# ▪ We achieve this by passing the arguments to the
# wrapper function
#
# ▪ The arguments will then be passed to the
# function that is being decorated at call time


def uppercase(n_letters):
    # This is a decorator factory. It creates and returns a decorator that takes
    # a function and modifies it to change the first n_letters of its output to uppercase.
    def decorator(function):
        # The actual decorator that wraps the function to enhance or modify its behavior.
        def wrapper():
            """from wrapper"""
            # Calls the original function and stores its output.
            result = function()
            # Converts the first n_letters of the result to uppercase.
            upper_part = result[:n_letters].upper()
            # Takes the remainder of the result string as it is.
            lower_part = result[n_letters:]
            # Concatenates the uppercased part with the rest and returns the new string.
            return upper_part + lower_part

        # Returns the wrapper function that will be called instead of the original function.
        return wrapper

    # Returns the decorator which will be applied to a function.
    return decorator


# The decorator is applied to this function with n_letters set to 4.
@uppercase(4)
def say_hi():
    # The function simply returns a greeting string.
    return "Hello there!"


# Prints the result of the decorated function, showcasing the effect of the decorator.
print(say_hi())
