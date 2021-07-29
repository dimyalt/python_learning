from openpyxl import *
import telebot
import time
from datetime import date
import pandas as pd


file = load_workbook("sample.xlsx")  # Открываем рабочую книгу / Opening the workbook
list_ = file.active  # Создали переменную для активного листа / Create a variable for the active sheet
file.iso_dates = True
data = []
start_date = ''
end_date = ''
get_name_game = ''
get_org_name = ''
get_name_user = ''


bot = telebot.TeleBot(
    '')  # Подключили токен телеграмм бота / We connected the bot's telegram token

#startdate = ''


#keyboard1 = telebot.types.ReplyKeyboardMarkup(<span class="hljs-keyword">True</span>, <span class="hljs-keyword">True</span>)
#keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])  # Обработка команды "start" / Processing the "start" command
def start_message(message):
    #otvet = types.InlineKeyboardMarkup(row_width=2)
    #button1 = types.InlineKeyboardButton(" Хорошо", callback_data='good')
    #button2 = types.InlineKeyboardButton(" Плохо", callback_data='bad')
    #otvet.add(button1, button2)
    #bot.send_message(message.chat.id,
                    # 'Привет, ты написал мне /start , более подробно узнать обо мне - пиши /help',
                    # reply_markup=keyboard1))  # Ответ бота на команду "start" / Bot response to "start" command
    #bot.send_message(message.chat.id,
                     #'Привет, ты написал мне /start , более подробно узнать обо мне - пиши /help',
                     #reply_markup=otvet)  # Ответ бота на команду "start" / Bot response to "start" command
    bot.send_message(message.chat.id,
                     'Привет, ты написал мне /start , более подробно узнать обо мне - пиши /help')  # Ответ бота на команду "start" / Bot response to "start" command

@bot.message_handler(commands=['help'])  # Обработка команды "help" / Processing the "help" command
def help_message(message):
    bot.send_message(message.chat.id, 'Написал мне /help - держи краткую справку:\nНапиши "игра" - получишь информацию '
                                      'про ближайшее мероприятие.\nНапиши "игры" - расскажу о ближайших 5 мероприятиях.\n'
                                      'Хочешь рассказать об игре - так и пиши - "добавить".\nРедактировать добавленную тобой '
                                      'информацию можно, написав "перенос" (не работает)')  # Ответ бота на команду "help" / Bot response to "help" command


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'добавить':
        global data

        data = []
        bot.send_message(message.from_user.id,
                         "Ok, давай добавим новый движ.. \nНапиши, когда начало (ддммгг, например:"
                         " 01012021):", );

        bot.register_next_step_handler(message, get_start_date);  # следующий шаг – функция get_start_date

    elif message.text.lower() == 'игра':
        current_date = date.today().strftime('%d.%m.%Y')
        current_date_sort = date.today().strftime('%Y-%m-%d')
        onegame(current_date_sort)
        one_game = onegame(current_date_sort)
        bot.send_message(message.from_user.id, f'Сегодня {current_date}\nБлижайшая игра c {one_game[0]} по {one_game[1]}\n'
                                               f'{one_game[2]} от {one_game[3]}\n'
                                               f'тип игры: {one_game[4]}\n');
        print(one_game)

    elif message.text.lower() == 'игры':
        current_date = date.today().strftime('%d.%m.%Y')
        current_date_sort = date.today().strftime('%Y-%m-%d')
        games(current_date_sort)
        many_games = games(current_date_sort)
        #print(games(current_date_sort))
        bot.send_message(message.from_user.id, f'Сегодня {current_date}\nБлижайшие мероприятия:\n1. С {many_games[0]} по {many_games[1]}\n'
                                               f'{many_games[2]} от {many_games[3]}\n'
                                               f'тип игры: {many_games[4]}\n2. С {many_games[5]} по {many_games[6]}\n'
                                               f'{many_games[7]} от {many_games[8]}\n'
                                               f'тип игры: {many_games[9]}\n3. С {many_games[10]} по {many_games[11]}\n'
                                               f'{many_games[12]} от {many_games[13]}\n'
                                               f'тип игры: {many_games[14]}\n4. С {many_games[15]} по {many_games[16]}\n'
                                               f'{many_games[17]} от {many_games[18]}\n'
                                               f'тип игры: {many_games[19]}\n5. С {many_games[20]} по {many_games[21]}\n'
                                               f'{many_games[22]} от {many_games[23]}\n'
                                               f'тип игры: {many_games[24]}\n');
    elif message.text.lower() == 'перенос':
        porting()
        bot.send_message(message.from_user.id, "Я еще не умею переносить =( Напиши /help.");
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.");

#print(startdate, 'startdate')
print('start')

def date_check(date):  # Функция проверки правильности написания даты
    try:
        date = time.strptime(date, '%d%m%Y')  # Если дата заполнена в формате ддммгггг
        true_date = time.strftime('%d.%m.%Y', date)  # Создаем переменную даты в формате дд.мм.гггг (для вывода пользователю)
        sort_date = time.strftime('%Y-%m-%d', date)  # Создаем переменную даты в формате гггг-мм-дд (для функции сортировки)
        return (true_date, sort_date)  # Возвращаем даты
    except ValueError: # Если дата не заполнена в формате ддммгггг появляется ошибка
        return False

def get_start_date(message):
    global start_date
    start_date = message.text
    if date_check(start_date) == False:
        bot.send_message(message.from_user.id, 'Неправильный формат даты! Попробуй еще раз (например 01012021):');
        bot.register_next_step_handler(message, get_start_date);
    else:
        user_date, sorting_date = date_check(start_date)
        data.append(user_date)
        data.append(sorting_date)
        #data.append(date_check(start_date))
        #data.append(date_check(start_date[1]))
        #sort_date = time.strftime('%d-%m-%Y', date_check(start_date))
        #data.append(sort_date)
        bot.send_message(message.from_user.id, 'Когда конец?');
        bot.register_next_step_handler(message, get_end_date);

def get_end_date(message):
    global end_date;
    end_date = message.text
    if date_check(end_date) == False:
        bot.send_message(message.from_user.id, 'Неправильный формат даты! Попробуй еще раз (например 01012021):');
        bot.register_next_step_handler(message, get_end_date);
    else:
        user_date, sorting_date = date_check(end_date)
        data.append(user_date)
        #data.append(date_check(end_date))
        bot.send_message(message.from_user.id, 'Название мероприятия?');
        bot.register_next_step_handler(message, get_name_game);

def get_name_game(message):
    global get_name_game;
    get_name_game = message.text;
    data.append(get_name_game)
    bot.send_message(message.from_user.id, 'Кто организатор?');
    bot.register_next_step_handler(message, get_orgname);
    print(data)

def get_orgname(message):
    global get_orgname;
    get_org_name = message.text;
    data.append(get_org_name)
    bot.send_message(message.from_user.id, 'Тип игры?');
    bot.register_next_step_handler(message, get_type_game);
    print(data)

def get_type_game(message):
    global get_type_game;
    global get_name_user;
    get_type_game = message.text;
    get_name_user = message.from_user.username;
    data.append(get_type_game)
    data.append(get_name_user)
    list_.append(data)
    file.save("sample.xlsx")
    sorting()
    bot.send_message(message.from_user.id, 'Ok, записал');
    print(list_, "list_", data, "data")


'''def onegame(current_date_sort):
    temp = []
    result = []
    search_date = current_date_sort
    #for row in range(2, list_.max_row + 1):
    #    for column in "B":  # Here you can add or reduce the columns
     #       cell_name = "{}{}".format(column, row)
            #print(cell_name)
            #list_[cell_name].value
     #       if list_[cell_name].value <= search_date:  # the value of the specific cell
      #          print(list_[cell_name].value)

    for i in range(1, list_.max_row):  # Для всех строк от 0 до максимальной
        for col in list_.iter_cols(2):  # Для всех колонок от 0 до максимальной
            #print(col[i].value)
            if col[i].value == search_date or col[i].value > search_date:
                for col in list_.iter_cols(1, list_.max_column):
                    temp.append(col[i].value)
    result.append(temp[0])
    result.append(temp[2])
    result.append(temp[3])
    result.append(temp[4])
    result.append(temp[5])
    return result'''

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
    df.to_excel(writer, sheet_name='testexel', columns=["Начало", "Сортировка", "Конец", "Название", "Организатор", "Тип", "Владелец"
    ], index=False)  # Выбираем какие столбцы записывать
    writer.save()  #  Сохраняем
    # Просмотр таблицы
    for i in range(0, list_.max_row):  # Для всех строк от 0 до максимальной
        for col in list_.iter_cols(1, list_.max_column):  # Для всех колонок от 0 до максимальной
            print(col[i].value, end="\t\t")  # Печатаем значение ячейки
        print('')

def porting():
    pass
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

    #for row in list_.iter_rows(min_row=list_row[0], max_col=6, max_row=list_row[4]):
    for row in list_.iter_rows(min_row=list_row[0], max_col=6, max_row=list_.max_row):  # Для диапазона начиная со строки
        # № которой идет 0 в списке дат и на протяжении всех столбцов
        for cell in row:  # Для всех ячеек
            temp.append(cell.value)  # Добавляем во временный список значение ячеек
    #print(len(temp))

    if len(temp) < 30:
        while len(temp) < 30:
            temp.append('-')
    #print(temp)

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
