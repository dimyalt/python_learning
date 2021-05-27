from random import choice
chars = ''


pass_leight = int(input('Введите длину пароля: '))
print(f'Длина пароля {pass_leight} символов.')
pass_number = int(input('Введите количество паролей: '))
numbers = input('Нужны ли цифры? [да/нет] ').lower() == 'да'
letters = input('Нужны ли буквы? [да/нет] ').lower() == 'да'
specials = input('Нужны ли знаки? [да/нет] ').lower() == 'да'
control = input('Нужен ли контроль символов (убрать похожие символы, типа 0 (ноль) и О /'
                '(большая буква о) и другие символы)? [да/нет] ').lower() == 'да'


digits = "23456789"
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = "ABCDEFGHIJKMNPQRSTUVWXYZ"
punctuation = '$!%&*+#-=?@^_'
controversial = "il1Lo0O"


def creating_password(num, let, spec, con):
    symbol_field = ''
    if num:
        symbol_field += digits
    if let:
        symbol_field += lowercase_letters
        symbol_field += uppercase_letters
    if spec:
        symbol_field += punctuation
    if con:
        symbol_field += controversial
    return choice(symbol_field)


for _ in range(pass_number):

    for _ in range(pass_leight):

        chars += creating_password(numbers, letters, specials, control)

    print(chars)
    chars = ''