from openpyxl import *
import time

def add_event():
    pass

def onegame():
    pass

def games():
    pass

def porting():
    pass

file = load_workbook("sample.xlsx")
list_ = file.active

print('Привет!')
print()
flag = True
action = input('Напиши команду ("Добавить" или "Игра": )').lower()
while flag == True:
    if action == 'добавить':
        #add_event()
        data = [input('Начало: '), input('Конец: '), input('Название: '), input('Организатор: '), input('Тип: '),
                input('Владелец: ')]
        list_.append(data)
        file.save("sample.xlsx")
        break
    elif action == 'игра':
        onegame()
    elif action == 'игры':
        games()
    elif action == 'перенос':
        porting()
    else:
        action = input('Напиши команду правильно: ').lower()
        flag == False


