from openpyxl import *
import time
import telebot

file = load_workbook("sample.xlsx")  # Открываем рабочую книгу / Opening the workbook
list_ = file.active  # Создали переменную для активного листа / Create a variable for the active sheet
data = []
start_date = ''
end_date = ''
get_name_game = ''
get_org_name = ''
get_name_user = ''

bot = telebot.TeleBot(
    '1638491301:AAHqxXK9Iem9rC2fSz5mPGv_hWmJrrTnaFk')  # Подключили токен телеграмм бота / We connected the bot's telegram token


@bot.message_handler(commands=['start'])  # Обработка команды "start" / Processing the "start" command
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, ты написал мне /start')  # Ответ бота на команду "start" / Bot response to "start" command


@bot.message_handler(commands=['help'])  # Обработка команды "help" / Processing the "help" command
def help_message(message):
    bot.send_message(message.chat.id, 'Написал мне /help - держи краткую справку:\nНапиши "игра" - получишь информацию '
                                      'про ближайшее мероприятие.\nНапиши "игры" - расскажу о ближайших 5 мероприятиях.\n'
                                      'Хочешь рассказать об игре - так и пиши - "добавить".\nРедактировать добавленную тобой '
                                      'информацию можно, написав "перенос"')  # Ответ бота на команду "help" / Bot response to "help" command


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'добавить':
        global data;
        data = []
        bot.send_message(message.from_user.id, "Ok, давай добавим новый движ.. \nНапиши, когда начало:");
        bot.register_next_step_handler(message, get_start_date);  # следующий шаг – функция get_start_date
    elif message.text.lower() == 'игра':
        onegame()
    elif message.text.lower() == 'игры':
        games()
    elif message.text.lower() == 'перенос':
        porting()
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.");


def get_start_date(message):
    global start_date;
    start_date = message.text;
    data.append(start_date)
    bot.send_message(message.from_user.id, 'Когда конец?');
    bot.register_next_step_handler(message, get_end_date);
    print(data)


def get_end_date(message):
    global end_date;
    end_date = message.text;
    data.append(end_date)
    bot.send_message(message.from_user.id, 'Название мероприятия?');
    bot.register_next_step_handler(message, get_name_game);
    print(data)


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
    bot.send_message(message.from_user.id, 'Ok, записал');
    print(list_, "list_", data, "data")


bot.polling(none_stop=True,
            interval=0)  # Опрос телеграмма на входящие сообщения / Telegram survey for incoming messages
