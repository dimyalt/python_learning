# Подключаемся к Binance Api
from binance import *
#from binance.client import Client
#from binance.websockets import BinanceSocketManager
# Работа со временем
import time
# Работа с вычислениями
from math import *

# Api key
api_key = '4BEhUO4zrqsauxoZIybqOCyZeYne2UXPFQnVAAIfQuZWxseoeiQRmVcn46vOkfmn'
#api_key = 'CEIZeCkIN6dgldSyQprhAUFJezMkrrkC4Bn9tKvlg7pmb44Z40XiahppH3jhT5sA'
# Secret Api key
api_secret = 'Jq7r4qu8jiGEEfs6aYdX09ar2tju4HKL9c8zpCpF5vuYzV0QwUsHTONIKSBMVbWT'
#api_secret = 'k4OeIeUDjv6AH5wAVcWZAXrkxO64wX3V8GE632TsQ1lzwxWSg00wodJ382RPMTGc'
# Client
client = Client(api_key, api_secret)

# Рынок
ASSET = 'ETHUSDT'
# Торгуемая валюта
CURRENCY = 'USDT'
# Торгуемая криптовалюта
CRYPTOCURRENCY = 'ETH'
# Стартовый капитал криптовалюты
START_CRYPTOCURRENCY = 0.10000000


#''' Б а л а н с '''


def balance(symbol):
    balance = client.get_asset_balance(asset=symbol)
#    balance = client.get_asset_balance(asset=symbol)
    balance = {'free': balance['free'], 'locked': balance['locked']}
    return balance


#''' И с т о р и я '''


def history(symbol):
    history = client.get_my_trades(symbol=symbol)
    return history


#''' К у р с '''


def price(symbol):
    price = client.get_avg_price(symbol=symbol)['price']
    return float(price)


#''' П о к у п к а '''


def order_market_buy(quantity):
    order = client.order_market_buy(symbol=ASSET, quantity=quantity)


#''' П р о д а ж а '''


def order_market_sell(quantity):
    order = client.order_market_sell(symbol=ASSET, quantity=quantity)


# Telegram bot
import telebot

# API бота
bot = telebot.TeleBot('1903362297:AAFITWA1R-U8ri_Z_WhaX-XPvdvUvnXfv1w')
# ID получателя в telegram
ID = '1205233811'

#''' С о о б щ е н и е '''


def message(text):
    bot.send_message(ID, text)


#''' С о о б щ е н и е П о к у п к и '''


def buy_message_success():
    # Получаем последнюю сделку
    data = history(ASSET)[-1]
    # Отправляем сообщения
    message('Покупка')
    message('Информация о сделке \n\nРынок: ' + data['symbol'] + '\nПокупка: ' + data[
        'commissionAsset'] + '\nКупленный актив: ' + data['qty'] + ' ' + data[
                'commissionAsset'] + '\nПроданный актив: ' + data[
                'quoteQty'] + ' ' + CURRENCY + '\nЦена на момент покупки: ' + data[
                'price'] + ' ' + CURRENCY + '\nКомиссия: ' + data[
                'commission'] + ' ' + CURRENCY + '\nВремя сделки: ' + str(data['time']))
    message('Информация о балансе \n\nБаланс ' + CURRENCY + ': ' + str(
        balance(CURRENCY)['free']) + '\nБаланс ' + CRYPTOCURRENCY + ': ' + str(balance(CRYPTOCURRENCY)['free']))
    message('Прибыль \n\nПрибыль ' + CRYPTOCURRENCY + ': ' + str(
        float(balance(CRYPTOCURRENCY)['free']) - START_CRYPTOCURRENCY))


#''' С о о б щ е н и е П р о д а ж и '''


def sell_message_success():
    # Получаем последнюю сделку
    data = history(ASSET)[-1]
    # Отправляем сообщения
    message('Продажа')
    message('Информация о сделке \n\nРынок: ' + data['symbol'] + '\nПокупка: ' + data[
        'commissionAsset'] + '\nКупленный актив: ' + data['quoteQty'] + ' ' + data[
                'commissionAsset'] + '\nПроданный актив: ' + data[
                'qty'] + ' ' + CRYPTOCURRENCY + '\nЦена на момент продажи: ' + data[
                'price'] + ' ' + CRYPTOCURRENCY + '\nКомиссия: ' + data[
                'commission'] + ' ' + CRYPTOCURRENCY + '\nВремя сделки: ' + str(data['time']))
    message('Информация о балансе \n\nБаланс ' + CURRENCY + ': ' + str(
        balance(CURRENCY)['free']) + '\nБаланс ' + CRYPTOCURRENCY + ': ' + str(balance(CRYPTOCURRENCY)['free']))
    message('Прибыль\n\nПрибыль ' + CRYPTOCURRENCY + ': ' + str(
        float(balance(CRYPTOCURRENCY)['free']) - START_CRYPTOCURRENCY))


# Время обновления курса
TIME = 10
# Процент при котором будет совершена  покупка
GROW_PERCENT = 0.5
# Процент при котором будет совершена продажа
FALL_PERCENT = -0.25

#''' А л г о р и т м '''


def main(FIRST_PRICE):
    # Функция обрезает число до n кол-во символов(Нужна чтобы при покупки и продажи не возникло ошибки)
    def toFixed(f: float, n=0):
        a, b = str(f).split('.')
        return '{}.{}{}'.format(a, b[:n], '0' * (n - len(b)))

    # Засыпаем
    time.sleep(TIME)
    # Получаем новую цену
    PRICE = price(ASSET)
    # Процентное изменение
    PROCENT = ((PRICE - FIRST_PRICE) / FIRST_PRICE) * 100

    print('Цена отсчета:', str(FIRST_PRICE), '| Процент:', str(PROCENT))
    #print(client.get_asset_balance(asset=CURRENCY))
    #print(client.get_asset_balance(asset=CRYPTOCURRENCY))
    # Покупка
    if PROCENT >= GROW_PERCENT:
        try:
            print('SELL')
            # Покупаем
            #order_market_buy(toFixed(float(balance(CURRENCY)['free']) / price(ASSET), 5))
            #order_market_buy(toFixed(float(balance(CURRENCY)['free']) / price(ASSET), 2))
            order_market_sell(toFixed(float(balance(CRYPTOCURRENCY)['free']), 1)) # !
            # Отправляем сообщение
            buy_message_success()
            # Перезапускаем функцию
            main(PRICE)
        except:
            print('Ошибка при покупке!')
            # Перезапускаем функцию
            main(PRICE)

    # Продажа
    elif PROCENT <= FALL_PERCENT:
        try:
            print('BUY', toFixed(float(balance(CRYPTOCURRENCY)['free'])))
            # Покупаем
            #order_market_sell(toFixed(float(balance(CRYPTOCURRENCY)['free']), 5))
            #order_market_sell(toFixed(float(balance(CRYPTOCURRENCY)['free']), 1))
            order_market_buy(toFixed(float(balance(CURRENCY)['free']) / price(ASSET), 2)) # !
            # Отправляем сообщение
            sell_message_success()
            # Перезапускаем функцию
            main(PRICE)
        except:
            print('Ошибка при продаже!')
            # Перезапускаем функцию
            main(PRICE)

    else:
        # Перезапускаем функцию
        main(FIRST_PRICE)


#''' З а п у с к '''
# Стартовые значения
START_PRICE = price(ASSET)
# Запускаем
main(START_PRICE)
