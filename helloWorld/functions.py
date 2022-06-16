def greet_user():
    print('Hi there')

# Parametre

def greet_user2(fname, nationality = 'French'):
    print(f'Hi {fname} {nationality}')

greet_user2('Mamadou','Omar')
greet_user2('Omar','Mamadou')

list = ['Sara', 'Tom', 'John']

for name in list:
    greet_user2(name)

# return statement

list_numbers = [1872, 11, 239, 192]
list_squred_numbers = []

def square(number):
    return number * number

for number in list_numbers:
    list_squred_numbers.append(square(number))


print(list_squred_numbers)