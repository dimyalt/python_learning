from openpyxl import *
import telebot
import time
from datetime import date
import pandas as pd
from telebot import types

file = load_workbook("sample.xlsx")  # Открываем рабочую книгу / Opening the workbook
list_ = file.active  # Создали переменную для активного листа / Create a variable for the active sheet
file.iso_dates = True
data = []
start_date = ''
end_date = ''
get_name_game = ''
get_org_name = ''
get_name_user = ''
id_game = ''

bot = telebot.TeleBot(
    'XXXXXXXX')  # Подключили токен телеграмм бота / We connected the bot's
# telegram token


@bot.message_handler(commands=['start'])  # Обработка команды "start" / Processing the "start" command
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    button_game = types.InlineKeyboardButton('Следующая игра', callback_data='игра')
    button_games = types.InlineKeyboardButton('Ближайшие игры', callback_data='игры')
    button_info = types.InlineKeyboardButton('Что-бы добавить - напиши "добавить"', callback_data='инфо')
    button_info2 = types.InlineKeyboardButton('Что-бы редактировать - напиши "перенос"', callback_data='инфо')
    # button_add = types.InlineKeyboardButton('Добавить мероприятие', callback_data='добавить')
    # button_porting = types.InlineKeyboardButton('Редактировать', callback_data='перенос')
    markup.row(button_game, button_games)
    markup.row(button_info)
    markup.row(button_info2)
    msg = bot.send_message(message.chat.id,
                           'Привет, ты написал мне /start , более подробно узнать обо мне - пиши /help',
                           reply_markup=markup)
    # Ответ бота на команду "start" / Bot response to "start" command
    print(msg)


@bot.message_handler(commands=['help'])  # Обработка команды "help" / Processing the "help" command
def help_message(message):
    bot.send_message(message.chat.id, 'Написал мне /help - держи краткую справку:\nНапиши "игра" - получишь информацию '
                                      'про ближайшее мероприятие.\nНапиши "игры" - расскажу о ближайших 5 мероприятиях.\n'
                                      'Хочешь рассказать об игре - так и пиши - "добавить".\nРедактировать добавленную тобой '
                                      'информацию можно, написав "перенос" (не работает)')  # Ответ бота на команду "help"
    # / Bot response to "help" command


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'добавить':
        global data

        data = []
        bot.send_message(message.from_user.id,
                         "Ok, давай добавим новый движ.. \nНапиши, когда начало (ддммгг, например:"
                         " 01012021):")

        bot.register_next_step_handler(message, get_start_date)  # следующий шаг – функция get_start_date

    elif message.text.lower() == 'игра':
        current_date = date.today().strftime('%d.%m.%Y')
        current_date_sort = date.today().strftime('%Y-%m-%d')
        onegame(current_date_sort)
        one_game = onegame(current_date_sort)
        bot.send_message(message.from_user.id, f'Сегодня {current_date}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \n'
                                               f'Ближайшая игра c {one_game[0]} по {one_game[1]}\n'
                                               f'{one_game[2]} от {one_game[3]}\n'
                                               f'тип игры: {one_game[4]}\n')
        print(one_game)

    elif message.text.lower() == 'игры':
        current_date = date.today().strftime('%d.%m.%Y')
        current_date_sort = date.today().strftime('%Y-%m-%d')
        games(current_date_sort)
        many_games = games(current_date_sort)
        # print(games(current_date_sort))
        bot.send_message(message.from_user.id, f'Сегодня {current_date}\nБлижайшие мероприятия:\n1. С {many_games[0]} '
                                               f'по {many_games[1]}\n'
                                               f'{many_games[2]} от {many_games[3]}\n'
                                               f'тип игры: {many_games[4]}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \n'
                                               f'2. С {many_games[5]} по {many_games[6]}\n'
                                               f'{many_games[7]} от {many_games[8]}\n'
                                               f'тип игры: {many_games[9]}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \n'
                                               f'3. С {many_games[10]} по {many_games[11]}\n'
                                               f'{many_games[12]} от {many_games[13]}\n'
                                               f'тип игры: {many_games[14]}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \n'
                                               f'4. С {many_games[15]} по {many_games[16]}\n'
                                               f'{many_games[17]} от {many_games[18]}\n'
                                               f'тип игры: {many_games[19]}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \n'
                                               f'5. С {many_games[20]} по {many_games[21]}\n'
                                               f'{many_games[22]} от {many_games[23]}\n'
                                               f'тип игры: {many_games[24]}\n')
    elif message.text.lower() == 'перенос':
        current_date_sort = date.today().strftime('%Y-%m-%d')
        user_list = porting(message, current_date_sort)
        for i in user_list:
            bot.send_message(message.from_user.id, f'ID {i[7]}\nС {i[0]} по {i[2]}\nНазвание: {i[3]}\nОрганизатор: '
                                                   f'{i[4]}\nТип: {i[5]}')
        bot.send_message(message.from_user.id, 'Какую запись редактируем? (Введи ID записи):')
        bot.register_next_step_handler(message, edit_buttons)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
# send_text(call)
def handle(call):
    # bot.send_message(call.message.chat.id, 'Data: {}'.format(str(call.data)))
    message = str(call.data)
    if message.lower() == 'игра':
        current_date = date.today().strftime('%d.%m.%Y')
        current_date_sort = date.today().strftime('%Y-%m-%d')
        onegame(current_date_sort)
        one_game = onegame(current_date_sort)
        bot.send_message(call.message.chat.id,
                         f'Сегодня {current_date}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \nБлижайшая игра c '
                         f'{one_game[0]} по {one_game[1]}\n'
                         f'{one_game[2]} от {one_game[3]}\n'
                         f'тип игры: {one_game[4]}\n')
        print(one_game)
    elif message.lower() == 'игры':
        current_date = date.today().strftime('%d.%m.%Y')
        current_date_sort = date.today().strftime('%Y-%m-%d')
        games(current_date_sort)
        many_games = games(current_date_sort)
        # print(games(current_date_sort))
        bot.send_message(call.message.chat.id, f'Сегодня {current_date}\nБлижайшие мероприятия:\n1. С {many_games[0]} '
                                               f'по {many_games[1]}\n'
                                               f'{many_games[2]} от {many_games[3]}\n'
                                               f'тип игры: {many_games[4]}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \n'
                                               f'2. С {many_games[5]} по {many_games[6]}\n'
                                               f'{many_games[7]} от {many_games[8]}\n'
                                               f'тип игры: {many_games[9]}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \n'
                                               f'3. С {many_games[10]} по {many_games[11]}\n'
                                               f'{many_games[12]} от {many_games[13]}\n'
                                               f'тип игры: {many_games[14]}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \n'
                                               f'4. С {many_games[15]} по {many_games[16]}\n'
                                               f'{many_games[17]} от {many_games[18]}\n'
                                               f'тип игры: {many_games[19]}\n\U0001F538 \U0001F538 \U0001F538 \U0001F538 \n'
                                               f'5. С {many_games[20]} по {many_games[21]}\n'
                                               f'{many_games[22]} от {many_games[23]}\n'
                                               f'тип игры: {many_games[24]}\n')
    elif message.lower() == 'название':
        result_name_type_game = line_address_detection(id_game, message)
        msg = bot.send_message(call.message.chat.id, f'Меняем название "{list_[result_name_type_game].value}" на:')
        bot.register_next_step_handler(msg, correct, result_name_type_game)

    elif message.lower() == 'тип':
        result_name_type_game = line_address_detection(id_game, message)
        msg = bot.send_message(call.message.chat.id, f'Меняем тип "{list_[result_name_type_game].value}" на:')
        bot.register_next_step_handler(msg, correct, result_name_type_game)

    elif message.lower() == 'отмена':
        result_cell_game = line_address_detection(id_game, message)
        result_cancel_game = int(result_cell_game[1:])
        bot.send_message(call.message.chat.id, f'Отмена мероприятия с ID: "{list_[result_cell_game].value}"')
        list_.delete_rows(result_cancel_game)
        file.save("sample.xlsx")
        sorting()
        bot.send_message(message.from_user.id, f'Удалено.')

    elif message.lower() == 'даты':
        result_name = line_address_detection(id_game, message)
        bot.send_message(call.message.chat.id, f'Меняем даты "{list_[result_name].value}" на:')

    print(message, 'calbackdata')
    print(type(message))



print('start')


def date_check(date):  # Функция проверки правильности написания даты
    try:
        date = time.strptime(date, '%d%m%Y')  # Если дата заполнена в формате ддммгггг
        true_date = time.strftime('%d.%m.%Y',
                                  date)  # Создаем переменную даты в формате дд.мм.гггг (для вывода пользователю)
        sort_date = time.strftime('%Y-%m-%d',
                                  date)  # Создаем переменную даты в формате гггг-мм-дд (для функции сортировки)
        return (true_date, sort_date)  # Возвращаем даты
    except ValueError:  # Если дата не заполнена в формате ддммгггг появляется ошибка
        return False


def get_start_date(message):
    global start_date
    start_date = message.text
    if date_check(start_date) == False:
        bot.send_message(message.from_user.id, 'Неправильный формат даты! Попробуй еще раз (например 01012021):')
        bot.register_next_step_handler(message, get_start_date)
    else:
        user_date, sorting_date = date_check(start_date)
        data.append(user_date)
        data.append(sorting_date)
        bot.send_message(message.from_user.id, 'Когда конец?')
        bot.register_next_step_handler(message, get_end_date)


def get_end_date(message):
    global end_date;
    end_date = message.text
    if date_check(end_date) == False:
        bot.send_message(message.from_user.id, 'Неправильный формат даты! Попробуй еще раз (например 01012021):')
        bot.register_next_step_handler(message, get_end_date)
    else:
        user_date, sorting_date = date_check(end_date)
        data.append(user_date)
        # data.append(date_check(end_date))
        bot.send_message(message.from_user.id, 'Название мероприятия?')
        bot.register_next_step_handler(message, get_name_game)


def get_name_game(message):
    global get_name_game;
    get_name_game = message.text
    data.append(get_name_game)
    bot.send_message(message.from_user.id, 'Кто организатор?')
    bot.register_next_step_handler(message, get_orgname)
    print(data)


def get_orgname(message):
    global get_orgname;
    get_org_name = message.text
    data.append(get_org_name)
    bot.send_message(message.from_user.id, 'Тип игры?')
    bot.register_next_step_handler(message, get_type_game)
    print(data)


def get_type_game(message):
    global get_type_game;
    global get_name_user;
    get_type_game = message.text
    get_name_user = message.from_user.username
    data.append(get_type_game)
    data.append(get_name_user)
    get_id_game()
    list_.append(data)
    file.save("sample.xlsx")
    sorting()
    bot.send_message(message.from_user.id, f'Ok, записал. \U0001F194 твоей записи {data[-1]}')
    print(list_, "list_", data, "data")


def get_id_game():
    global get_id_game;
    # id_cell = list_.cell(row=list_.max_row, column=list_.max_column - 1)
    id_cell = 1  # Переменная, в которую запишем максимальное значение ID
    for row in range(2, list_.max_row + 1):  # Для строк со второй и до последней
        for column in "H":  # Для столбца H в котором указан ID
            cell_name = "{}{}".format(column, row)  # Получаем адрес ячейки
            if list_[cell_name].value > id_cell:  # Если значение ячейки больше значения id_cell
                id_cell = list_[cell_name].value  # Присваеваем значение ячейки переменной id_cell
    data.append(id_cell + 1)


def onegame(current_date_sort):
    temp = []  # Временный массив
    result = []  # Результат
    list_row = []  # Список со значениями номера ячеек, даты которых больше текущей даты
    search_date = current_date_sort  # Дата поиска = переданному значению

    for row in range(2, list_.max_row + 1):  # Для строк со второй и до последней
        for column in "B":  # Для столбца B в котором указана дата в формате для поиска ГГГГ-мм-дд
            cell_name = "{}{}".format(column, row)  # Получаем адрес ячейки
            if list_[cell_name].value >= search_date:  # Если значение ячейки больше или равно текущей дате
                list_row.append(row)  # Значение ячейки добавляем в список

    for row in list_.iter_rows(min_row=list_row[0], max_col=6, max_row=list_row[0]):  # Для диапазона начиная со строки
        # № которой идет 0 в списке дат и на протяжении всех столбцов
        for cell in row:  # Для всех ячеек
            temp.append(cell.value)  # Добавляем во временный список значение ячеек

    result.append(temp[0])  # Добавляем в итоговый список значение начала
    result.append(temp[2])  # Добавляем в итоговый список значение конца
    result.append(temp[3])  # Добавляем в итоговый список значение названия
    result.append(temp[4])  # Добавляем в итоговый список значение организатора
    result.append(temp[5])  # Добавляем в итоговый список значение типа

    return result


def sorting():
    xl = pd.ExcelFile("sample.xlsx")  # Открываем pandas наш файл
    df = xl.parse("testexel")  # Открываем pandas активный лист
    df = df.sort_values(by="Сортировка")  # Сортируем по возрастанию столбец Сортировка (sort_date ('%Y-%m-%d'))
    writer = pd.ExcelWriter('sample.xlsx')  # Записываем файл
    df.to_excel(writer, sheet_name='testexel', columns=["Начало", "Сортировка", "Конец", "Название", "Организатор",
                                                        "Тип", "Владелец", "ID"],
                index=False)  # Выбираем какие столбцы записывать
    writer.save()  # Сохраняем
    # Просмотр таблицы
    for i in range(0, list_.max_row):  # Для всех строк от 0 до максимальной
        for col in list_.iter_cols(1, list_.max_column):  # Для всех колонок от 0 до максимальной
            print(col[i].value, end="\t\t")  # Печатаем значение ячейки
        print('')


def porting(message, current_date_sort):
    global get_name_user;
    search_date = current_date_sort  # Дата поиска = переданному значению
    temp_name = []
    temp_date = []
    temp_result = []
    temp = []
    get_name_user = message.from_user.username  # Получаем имя пользователя, написавшего сообщение
    for row in range(2, list_.max_row + 1):  # Для строк со второй и до последней
        for column in "G":  # Для столбца G в котором указано имя пользователя, создавшего запись
            cell_name = "{}{}".format(column, row)  # Получаем адрес ячейки
            if list_[cell_name].value == get_name_user:  # Если значение ячейки равно имени пользователя
                temp_name.append(row)  # Значение ячейки добавляем в список
    print(temp_name)
    for row in range(2, list_.max_row + 1):  # Для строк со второй и до последней
        for column in "B":  # Для столбца B в котором указана дата в формате для поиска ГГГГ-мм-дд
            cell_name = "{}{}".format(column, row)  # Получаем адрес ячейки
            if list_[cell_name].value >= search_date:  # Если значение ячейки больше или равно текущей дате
                temp_date.append(row)  # Значение ячейки добавляем в список
    print(temp_date)
    for i in temp_name:
        if i in temp_date:
            temp_result.append(i) # Итоговое значение ячейки добавляем в список
    print(temp_result)


    for row in list_.iter_rows(min_row=temp_result[0], max_col=8, max_row=list_.max_row):  # Для диапазона начиная со строки
            # № которой идет 0 в списке и на протяжении всех столбцов
       for cell in row:  # Для всех ячеек
            temp.append(cell.value)  # Добавляем во временный список значение ячеек

    sep = 8  # кол-во элементов в одном внутреннем списке
    result = [temp[x:x + sep] for x in range(0, len(temp), sep)]
    print(temp)
    print(result)
    return(result)

'''def edit_game(message):
    id_game = message.text
    print(id_game)'''

def edit_buttons(message):
    global id_game
    id_game = message.text # В месседже получаем ID игры, которую будем редактировать
    markup = types.InlineKeyboardMarkup()
    button_startend_game = types.InlineKeyboardButton('Даты проведения', callback_data='даты')
    #  button_end_game = types.InlineKeyboardButton('Конец', callback_data='конец')
    button_name_game = types.InlineKeyboardButton('Название', callback_data='название')
    button_type_game = types.InlineKeyboardButton('Тип', callback_data='тип')
    button_cancel_game = types.InlineKeyboardButton('Отмена', callback_data='отмена')
    markup.row(button_startend_game, button_name_game)
    markup.row(button_type_game, button_cancel_game)
    #print(id_game, 'id_game')
    bot.send_message(message.chat.id, 'Выбери что редактируем?', reply_markup=markup)
    #editing(call)

    #bot.register_next_step_handler(message, editing)
    # @bot.callback_query_handler(func=lambda call: True)

def line_address_detection(id_game, message):
    #print(id_game, 'id_game')
    #print(message, 'message')
    #bot.send_message(call.message.chat.id, f'Название {id_game}')
    for row in range(2, list_.max_row + 1):  # Для строк со второй и до последней
        for column in "H":  # Для столбца H в котором указано ID мероприятия
            cell_name = "{}{}".format(column, row)  # Получаем адрес ячейки
            string_num = "{}".format(row)  # Получаем номер строки
            #print(cell_name)
            #print(list_[cell_name].value)
            if str(list_[cell_name].value) == id_game:  # Если значение в ячейке совпадает с введенным ID
                if message == 'название':
                #print(list_[cell_name].value)
                    name_cell_adr = 'D' + string_num  #  Создаем переменную с адресом ячейки с названием мероприятия
                elif message == 'тип':
                    name_cell_adr = 'F' + string_num  # Создаем переменную с адресом ячейки с типом мероприятия
                elif message == 'отмена':
                    name_cell_adr = 'H' + string_num  # Создаем переменную с адресом ячейки с ID мероприятия
                elif message == 'даты':
                    name_cell_adr = 'A' + string_num  # Создаем переменную с адресом ячейки с началом мероприятия
                #print(cell_name)
                #print(string_num)
                #print(name_cell_adr, list_[name_cell_adr].value)
                #bot.send_message(message.chat.id, list_[name_cell_adr].value, 'Заменить на:')
                return(name_cell_adr)  # Возвращает адрес ячейки

def correct(message, result_name_type_game):
    print(message.text, 'message', result_name_type_game, 'result_name_type_game')
    list_[result_name_type_game] = message.text
    file.save("sample.xlsx")
    sorting()
    bot.send_message(message.from_user.id, f'Ok, записал.')


def games(current_date_sort):
    temp = []  # Временный массив
    result = []  # Результат
    list_row = []  # Список со значениями номера ячеек, даты которых больше текущей даты
    search_date = current_date_sort  # Дата поиска = переданному значению

    for row in range(2, list_.max_row + 1):  # Для строк со второй и до последней
        for column in "B":  # Для столбца B в котором указана дата в формате для поиска ГГГГ-мм-дд
            cell_name = "{}{}".format(column, row)  # Получаем адрес ячейки
            if list_[cell_name].value >= search_date:  # Если значение ячейки больше или равно текущей дате
                list_row.append(row)  # Значение ячейки добавляем в список

    # for row in list_.iter_rows(min_row=list_row[0], max_col=6, max_row=list_row[4]):
    for row in list_.iter_rows(min_row=list_row[0], max_col=6,
                               max_row=list_.max_row):  # Для диапазона начиная со строки
        # № которой идет 0 в списке дат и на протяжении всех столбцов
        for cell in row:  # Для всех ячеек
            temp.append(cell.value)  # Добавляем во временный список значение ячеек
    # print(len(temp))

    if len(temp) < 30:
        while len(temp) < 30:
            temp.append('-')
    # print(temp)

    result.append(temp[0])  # Добавляем в итоговый список значение начала
    result.append(temp[2])  # Добавляем в итоговый список значение конца
    result.append(temp[3])  # Добавляем в итоговый список значение названия
    result.append(temp[4])  # Добавляем в итоговый список значение организатора
    result.append(temp[5])  # Добавляем в итоговый список значение типа

    result.append(temp[6])  # Добавляем в итоговый список значение начала второй игры
    result.append(temp[8])  # Добавляем в итоговый список значение конца второй игры
    result.append(temp[9])  # Добавляем в итоговый список значение названия второй игры
    result.append(temp[10])  # Добавляем в итоговый список значение организатора второй игры
    result.append(temp[11])  # Добавляем в итоговый список значение типа второй игры

    result.append(temp[12])  # Добавляем в итоговый список значение начала третьей игры
    result.append(temp[14])  # Добавляем в итоговый список значение конца третьей игры
    result.append(temp[15])  # Добавляем в итоговый список значение названия третьей игры
    result.append(temp[16])  # Добавляем в итоговый список значение организатора третьей игры
    result.append(temp[17])  # Добавляем в итоговый список значение типа третьей игры

    result.append(temp[18])  # Добавляем в итоговый список значение начала четвертой игры
    result.append(temp[20])  # Добавляем в итоговый список значение конца четвертой игры
    result.append(temp[21])  # Добавляем в итоговый список значение названия четвертой игры
    result.append(temp[22])  # Добавляем в итоговый список значение организатора четвертой игры
    result.append(temp[23])  # Добавляем в итоговый список значение типа четвертой игры

    result.append(temp[24])  # Добавляем в итоговый список значение начала пятой игры
    result.append(temp[26])  # Добавляем в итоговый список значение конца пятой игры
    result.append(temp[27])  # Добавляем в итоговый список значение названия пятой игры
    result.append(temp[28])  # Добавляем в итоговый список значение организатора пятой игры
    result.append(temp[29])  # Добавляем в итоговый список значение типа пятой игры

    return result


bot.polling(none_stop=True,
            interval=0)  # Опрос телеграмма на входящие сообщения / Telegram survey for incoming messages
