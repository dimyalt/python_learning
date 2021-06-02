what = input('Это программа для работы с шифром Цезаря.\nМы шифруем или дешифруем? [да/нет]: ').lower() == 'да'
lang = input('Язык текста (напечатайте [рус/англ]): ') == 'рус'
if lang:
    step = int(input('Шаг сдвига шифра (31 - максимум): '))
    lowercase_letters_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    uppercase_letters_rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
else:
    step = int(input('Шаг сдвига шифра (26 - максимум): '))
    lowercase_letters_eng = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input('Введите текст для шифровки/дешифровки: ')


def encrypting(lang_en):
    code = []
    result = ''
    if lang_en:
        alphabet_leight = 32
        lowercase_letters = lowercase_letters_rus
        uppercase_letters = uppercase_letters_rus
    else:
        alphabet_leight = 26
        lowercase_letters = lowercase_letters_eng
        uppercase_letters = uppercase_letters_eng

    for i in range(len(text)):
        symbol = text[i]
        if uppercase_letters.find(symbol) != -1:
            temp_char = uppercase_letters.find(symbol) + step
            if temp_char >= alphabet_leight:
                temp_char -= alphabet_leight
            result += uppercase_letters[temp_char]
            code.append(temp_char)
        elif lowercase_letters.find(symbol) != -1:
            temp_char = lowercase_letters.find(symbol) + step
            if temp_char >= alphabet_leight:
                temp_char -= alphabet_leight
            result += lowercase_letters[temp_char]
            code.append(temp_char)
        elif not symbol.isalpha():
            temp_char = symbol.isalpha()
            code.append(symbol)
            result += symbol
    return result


def decrypting(lang_en, step):
    temp_char = 0
    code = []
    result = ''
    if lang_en:
        alphabet_leight = 32
        lowercase_letters = lowercase_letters_rus
        uppercase_letters = uppercase_letters_rus
    else:
        alphabet_leight = 26
        lowercase_letters = lowercase_letters_eng
        uppercase_letters = uppercase_letters_eng

    for i in range(len(text)):
        symbol = text[i]
        if uppercase_letters.find(symbol) != -1:
            temp_char = uppercase_letters.find(symbol) - step
            if temp_char > alphabet_leight:
                temp_char -= alphabet_leight
            result += uppercase_letters[temp_char]
            code.append(temp_char)
        elif lowercase_letters.find(symbol) != -1:
            temp_char = lowercase_letters.find(symbol) - step
            if temp_char > alphabet_leight:
                temp_char -= alphabet_leight
            result += lowercase_letters[temp_char]
            code.append(temp_char)
        elif symbol.isalpha() != True:
            temp_char = symbol.isalpha()
            code.append(symbol)
            result += symbol
    return result


if what:
    print('Ок. Шифруем...')
    print(encrypting(lang))

else:
    print('Приступаем к дешифровке...')
    if step == 0:
        for i in range(25):
            step = i
            print(decrypting(lang, step))
    else:
        print(decrypting(lang, step))
