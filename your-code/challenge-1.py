def plus(x, y):
    print(f"Your answer is: {x+y}")
def minus(x, y):
    print(f"Your answer is: {x-y}")

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

dict1 = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

first = 0
for key,value in dict1.items():
    if key == a:
        first +=value
        
second = 0
for key,value in dict1.items():
    if key == c:
        second+=value
        
if b == 'plus':
    plus(first, second)
elif b == 'minus':
    minus(first, second)
    
print("Thanks for using this calculator, goodbye :)")
