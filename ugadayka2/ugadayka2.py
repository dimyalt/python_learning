# -*- coding: utf-8 -*-
from random import *

x = randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(character):
    if character.isdigit() == True and 0 < int(character) < 101 :
        return True
    else:
        return False    

while True:   
    y = input('Введите число: ')
    while is_valid(y) != True:   
        y = input('А может быть все-таки введем целое число от 1 до 100?\n')
    else:
        y = int(y)
    
    if x < y:
        print('Слишком много, попробуйте еще раз!')
        continue
    elif x > y:
        print('Слишком мало, попробуйте еще раз!')
        continue
    else:    
        print('Вы угадали, поздравляем!')
        break  
