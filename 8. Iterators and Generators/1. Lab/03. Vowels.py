class Vowels:
    def __init__(self, text: str):
        self.text = text
        vowels_const = ["a", "i", "e", "u", "y", "o"]
        self.found_vowels = [char for char in self.text if char.lower() in vowels_const]
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.found_vowels):
            raise StopIteration
        result = self.found_vowels[self.current_index]
        self.current_index += 1
        return result


# Test Code

my_string = Vowels('Abcedifuty0o')

for char in my_string:
    print(char)
