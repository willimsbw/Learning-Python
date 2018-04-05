squares = set()

# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers
number = 1
while number**2 < 2000:
    squares.add(number**2)
    number += 1

print(squares)
