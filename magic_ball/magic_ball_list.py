# -*- coding: utf-8 -*-
from random import *
x = randrange(1, 21)
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как вас зовут? \nМеня зовут: ')
flag = True

def loop_questions():
    question = input(f'Задавай свой вопрос, {name}: ')
    answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    print(choice(answers))
    if is_new_game() == False:
        return False

def is_new_game():
    new_game = input('Хочешь задать еще вопрос? (Да / Нет): ')
    if new_game == 'Да' or new_game == 'ДА' or new_game == 'да':
        loop_questions()
    else:
        return False

while flag == True:
    question = input(f'Приветствую тебя. Задавай свой вопрос, {name}: ')
    answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    print(choice(answers))
    flag = is_new_game()





