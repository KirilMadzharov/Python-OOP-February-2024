"""
@property
@staticmethod
@classmethod
"""

# ▪ @classmethod- decorator function that converts a
# method to a class method
#
# ▪ @abstractmethod- decorator function that converts
# an instance method to an abstract instance method
#
# ▪ @abstractclassmethod- decorator function that
# converts a class method to an abstract class method
#
# ▪ @property- change your class methods/attributes
# so that the user of a class doesn't need to make any
# change in their code


"""
Example: property decorator
"""


class Person:
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


"""
Classes as Decorators

@Fibonacci
"""

# ▪ We can also use classes as decorators
#
# ▪ We usually do that when we need to maintain
# a state
#
# ▪ To use a class as a decorator, we need to
# implement the __call__method
#
# ▪ The __call__method allows class instances to
# be called as functions

"Example: __call__ method (1)"


class Fibonacci:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self(n - 1) + self(n - 2)
        return self.cache[n]


"Example: __call__ method"

fib = Fibonacci()

for i in range(5):
    print(fib(i))

    print(fib.cache)

# 0
# 1
# 1
# 2
# 3
# {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}


"Example: Class Decorator (1)"


class func_logger:
    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args)


"Example: Class Decorator (2)"


@func_logger
def say_hi(name):
    print(f"Hi, {name}")


@func_logger
def say_bye(name):
    print(f"Bye, {name}")


say_hi("Peter")
say_bye("Peter")
