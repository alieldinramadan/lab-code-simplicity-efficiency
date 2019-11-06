import random
import string
import sys
def RandomStringGenerator(l=12):
    randomer = string.ascii_lowercase + string.digits
    p = 0
    s = ''
    while p<l:
        s += random.choice(randomer)
        p += 1
    return s

def BatchStringGenerator(number, minimum=8, maximum=12):
    r = []
    for i in range(number):
        length = None
        if minimum < maximum:
            length = random.choice(range(minimum, maximum))
        elif minimum == maximum:
            length = minimum
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(length))
    return r

minimum = input('Enter minimum string length: ')
maximum = input('Enter maximum string length: ')
number = input('How many random strings to generate? ')

print(BatchStringGenerator(int(number), int(minimum), int(maximum)))