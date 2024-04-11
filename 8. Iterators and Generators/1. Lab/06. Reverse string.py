def reverse_text(txt):
    current = len(txt) - 1
    end = 0

    while current >= end:
        yield txt[current]
        current -= 1






for char in reverse_text("pets"):
    print(char, end='')
