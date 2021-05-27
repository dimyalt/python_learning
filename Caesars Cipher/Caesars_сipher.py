what = input('Это программа для работы с шифром Цезаря.\nМы шифруем или дешифруем? [да/нет]: ').lower() == 'да'
lang = input('Язык текста (напечатайте [рус/англ]): ') == 'рус'
if lang:
    step = int(input('Шаг сдвига шифра (32 - максимум): '))
    lowercase_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    uppercase_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
else:
    step = int(input('Шаг сдвига шифра (26 - максимум): '))
    lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
text = input('Введите текст для шифровки/дешифровки: ')


code = ''



def encrypting(lang_en, what_en, step_en):
    temp_char = ''
    for i in range(len(lowercase_letters)):
        #print(ord(text[i]))
        if lowercase_letters[i] in text: # or text[i] in uppercase_letters:
            print(lowercase_letters[i] + step)
            temp_char = i + step
            #code += (text[i] + step)
        #return code
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