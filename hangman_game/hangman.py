word = 'должность'
word_list = list(word)
#print(word_list)
wordlist = ['-' for _ in range(len(word_list))]
error = 0



def check_word(def_letter):
    if def_letter in word_list:
        #print(def_letter, 'def_letter check_word')
        return def_letter
    else:
        return 0


def show_word(def_letter):
    for i in range(len(word_list)):
        if def_letter == word_list[i]:
            del wordlist[i]
            wordlist.insert(i, def_letter)
    return wordlist


def building(def_error):
    if def_error == 0:
        print('--------\n|\n|\n|\n|\n|\n_')
    elif def_error == 1:
        print('--------\n|      |\n|\n|\n|\n|\n_')
    elif def_error == 2:
        print('--------\n|      |\n|      о\n|\n|\n|\n_')
    elif def_error == 3:
        print('--------\n|      |\n|      о\n|      |\n|\n|\n_')
    elif def_error == 4:
        print('--------\n|      |\n|      о\n|     /|\ \n|\n|\n_')
    elif def_error == 5:
        print('--------\n|      |\n|      о\n|     /|\ \n|     / \ \n|\n_')


while True:
    if error != 5:
        print('Слово: ', *wordlist)
        building(error)
        letter = input('Введите букву: ').lower()
        show_word(check_word(letter))

        if check_word(letter) == 0:
            error += 1
    else:
        print('Очень жаль, вы проиграли...')
        print('Загаданное слово: ', word)
        break









