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


def building(def_error, counter=0):
    pass

while True:

    #print('Слово: ', *show_word(check_word(letter)))
    print('Слово: ', *wordlist)
    letter = input('Введите букву: ').lower()
    show_word(check_word(letter))
    if check_word(letter) == 0:
        error += 1
    print(check_word(letter), 'def letter')
    print(error, 'error')
    #print(show_word(check_word(letter)))
    #print(letter)








