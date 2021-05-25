from random import *
x = randint(1, 100)
print(x)
print('Добро пожаловать в числовую угадайку')
y = input()

def is_valid(character):
    if character.isdigit() == True and 0 < int(character) < 101 :
        print('True')
        return True
    else:
        print('false')
        return False        

is_valid(y)    