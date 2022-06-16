

# si je rentre pas un int
# je vais avoir une exception error

try:
    age = int(input('How old are you ? '))
except ValueError:
    print('Invalid value')

try:
    number = int(input('Give a us a number'))
    result = 1000/number
    print(result)
except ZeroDivisionError:
    print('Impossible de diviser par 0')
