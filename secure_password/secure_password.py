from random import choice

print('Добро пожаловать в генератор паролей v.1.0')

pass_leight = int(input('Введите длину пароля: '))
print(f'Длина пароля {pass_leight} символов.')
numbers = input('Нужны ли цифры? [да/нет] ').lower() == 'да'
letters = input('Нужны ли буквы? [да/нет] ').lower() == 'да'
specials = input('Нужны ли знаки? [да/нет] ').lower() == 'да'
summary = []
print(numbers, 'numbers')

def creating_password(numb, lett, spec):
    numbers_list = list(range(48, 58))
    letters_list = list(range(65, 91))
    letters_list_2 = list(range(97, 123))
    specials_list = list(range(33, 48))
    specials_list_2 = list(range(91, 96))
    result_list = []

    if numb:
        result_list.extend(numbers_list)
    if lett:
        result_list.extend(letters_list)
        result_list.extend(letters_list_2)
    if spec:
        result_list.extend(specials_list)
        result_list.extend(specials_list_2)
    return choice(result_list)

for _ in range(pass_leight):
    summary.append(chr(creating_password(numbers, letters, specials)))
print('Ваш пароль: ', *summary, sep='')