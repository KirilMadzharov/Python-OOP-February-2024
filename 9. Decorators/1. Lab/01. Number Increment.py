def number_increment(numbers):
    def increase():
        return [i + 1 for i in numbers]

    return increase()


#Test Code

print(number_increment([1, 2, 3]))
