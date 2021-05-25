# -*- coding: utf-8 -*-
from random import *


print('Добро пожаловать в числовую угадайку')
newgame = True

top_border = input('Введите максимальное число (по умолчанию 100): ')
if top_border.isdigit() != True:
    top_border = 100
else:
    top_border = int(top_border)
    
while newgame != False:
    x = randint(1, top_border)
    print(x)
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
        
    print('Начать новую игру? Напечатай "ДА", если хочешь продолжить.')
    new_start = input()
    
    if new_start == 'ДА' or new_start == 'Да' or new_start == 'да':   
        newgame = True
    else:
        print('До встречи.')    
        break
      
