# -*- coding: utf-8 -*-
from random import *

x = randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(character):
    if character.isdigit() == True and 0 < int(character) < 101 :
        return True
    else:
        return False 
    
    
counter = 0
while True:   
    y = input('Введите число: ')
    while is_valid(y) != True:   
        y = input('А может быть все-таки введем целое число от 1 до 100?\n')
    else:
        y = int(y)

    if x < y:
        print('Слишком много, попробуйте еще раз!')
        counter += 1
        continue
    elif x > y:
        print('Слишком мало, попробуйте еще раз!')
        counter += 1
        continue
    else:    
        counter += 1
        print('Вы угадали, поздравляем!')
        print(f'Спасибо, что играли в числовую угадайку. Было: {counter} попыток. Еще увидимся...')
        break  
