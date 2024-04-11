class custom_range:
    def __init__(self, start, end):
        self.start = start -1
        self.end = end -1

    def __iter__(self):
        return self  # self is one_to_ten

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        self.start += 1
        return self.start


# Test Code

one_to_ten = custom_range(1, 10)

for num in one_to_ten:
    print(num)
