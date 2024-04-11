"""
GENERATORS
"""

"""
Generators are a simple way of creating iterators

▪ A generator is a function that returns an object (iterator)
▪ This iterator can later be iterated over (one value at a time
"""


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_first_n = sum(first_n(5))
print(sum_first_n)

"""
The yield Statement

▪ If a function contains at least one yield statement, it becomes a generator function
▪ Both yield and return will return a value from a function
▪ The difference between yield and return is that the return statement terminates a function entirely
▪ Yield, however, pauses the function saving all its states, and later continues from there on successive calls
"""

"""
Generators vs Normal Functions

▪ Generator function contains one or more yield statements
▪ It returns an iterator but does not start execution immediately
▪ Methods like __iter__()and __next__() are implemented automatically
▪ Once the function yields, the function is paused
▪ When the function terminates, StopIterationis raised automatically on further calls
"""


def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


for num in my_gen():
    print(num)

"""
Generator Expression

▪ Generators can be easily created using generator expressions
▪ Same as lambda function creates an anonymous function, generator expression creates an anonymous generator function
▪ The syntax for generator expression is similar to that of a list comprehension
▪ The difference between them is that generator expression produces one item at a time
"""

# Initialize the list
my_list = [1, 3, 6, 10]
# square each term using list comprehension
# Output: [1, 9, 36, 100]
print([x ** 2 for x in my_list])
# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
print((x ** 2 for x in my_list))
