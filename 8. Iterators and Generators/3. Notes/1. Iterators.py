"""
What are Iterators?
"""

"""
__iter__()and __next__()

▪ Iterator is simply an object that can be iterated upon
▪ An object which will return data, one element at a time
▪ Iterator object must implement two methods,
__iter__() and __next__()(iterator protocol)
▪ An object is called iterable if we can get an iterator
from it
▪ Such are: list, tuple, string, etc...
"""

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num


# Using the iterator
countdown = Countdown(5)
for number in countdown:
    print(number)
