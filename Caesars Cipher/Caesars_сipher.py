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
    code = ''
    for i in range(len(lowercase_letters)):
        if lowercase_letters[i] in text:
            temp_char = i + step_en
            if temp_char > 26:
                temp_char -= 26
            code += lowercase_letters[temp_char]
        if uppercase_letters[i] in text:
            temp_char = i + step_en
            if temp_char > 26:
                temp_char -= 26
            code += uppercase_letters[temp_char]
    return code
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