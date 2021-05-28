what = input('Это программа для работы с шифром Цезаря.\nМы шифруем или дешифруем? [да/нет]: ').lower() == 'да'
lang = input('Язык текста (напечатайте [рус/англ]): ') == 'рус'
if lang:
    step = int(input('Шаг сдвига шифра (32 - максимум): '))
    lowercase_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    uppercase_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
else:
    step = int(input('Шаг сдвига шифра (26 - максимум): '))
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input('Введите текст для шифровки/дешифровки: ')

def encrypting(lang_en, what_en, step_en):
    temp_char = 0
    code = []
    result = ''
    if lang_en:
        for i in range(len(text)):
            symbol = text[i]
            if uppercase_letters.find(symbol) != -1:
                temp_char = uppercase_letters.find(symbol) + step
                if temp_char > 33:
                    temp_char -= 33
                result += uppercase_letters[temp_char]
                code.append(temp_char)
            elif lowercase_letters.find(symbol) != -1:
                temp_char = lowercase_letters.find(symbol) + step
                if temp_char > 33:
                    temp_char -= 33
                result += lowercase_letters[temp_char]
                code.append(temp_char)
            elif symbol.isalpha() != True:
                temp_char = symbol.isalpha()
                code.append(symbol)
                result += symbol
    else:
        for i in range(len(text)):
            symbol = text[i]
            if uppercase_letters.find(symbol) != -1:
                temp_char = uppercase_letters.find(symbol) + step
                if temp_char > 26:
                    temp_char -= 26
                result += uppercase_letters[temp_char]
                code.append(temp_char)
            elif lowercase_letters.find(symbol) != -1:
                temp_char = lowercase_letters.find(symbol) + step
                if temp_char > 26:
                    temp_char -= 26
                result += lowercase_letters[temp_char]
                code.append(temp_char)
            elif symbol.isalpha() != True:
                temp_char = symbol.isalpha()
                code.append(symbol)
                result += symbol
    return result

def decrypting(lang_en, what_en, step_en):
    pass
#print(encrypting(lang, what, step))
#print(decrypting(lang, what, step))



if what:
    print('Ок. Шифруем...')
    print(encrypting(lang, what, step))
else:
    print('Приступаем к дешифровке...')
    print(decrypting(lang, what, step))