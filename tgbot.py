import telebot
import os
from telebot.types import Message
from urllib3 import request
import sqlite3
import datetime
import time
import threading
import os
from dotenv import load_dotenv

import nesco_balance_checker as main

load_dotenv()
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY, parse_mode='MARKDOWN')

command_name = ''

@bot.message_handler(commands=['start'])
def balance(message):
    global command_name
    command_name = 'balance'
    bot.send_message(message.chat.id, '''/balance - Check current balance\n
/balance_default - Check current balance with preset customer no.\n
/last_recharge - Check last recharge details\n
/last_recharge_default - Check last recharge details with preset customer no.\n
/notify - Notify if balance is less than ৳ 100\n
/notify_daily - Get balance update daily at 12:00 AM''')


@bot.message_handler(commands=['balance'])
def balance(message):
    global command_name
    command_name = 'balance'
    bot.send_message(message.chat.id, 'Enter a customer number.')


@bot.message_handler(commands=['last_recharge'])
def recharge(message):
    global command_name
    command_name = 'recharge'
    bot.send_message(message.chat.id, 'Enter a customer number.')


@bot.message_handler(commands=['notify'])
def notify(message):
    global command_name
    command_name = 'notify'
    bot.send_message(message.chat.id, 'Enter a customer number.')


@bot.message_handler(commands=['notify_daily'])
def notify(message):
    global command_name
    command_name = 'notify_daily'
    bot.send_message(message.chat.id, 'Enter a customer number.')


@bot.message_handler(commands=['last_recharge_default'])
def last_rechrage_default(message):
    global command_name
    command_name = 'last_recharge_default'

    x = check_database(message.chat.id, 7)

    if x == None:
        bot.send_message(message.chat.id, 'Enter a customer number.  (This step is only for initialization)')
    else:
        msg = bot.send_message(message.chat.id, 'Getting data...')
        response = balance_rechargeHistory('recharge', message=message, cust_no=x)[0]

        if response != False:
            bot.edit_message_text(response, message.chat.id, msg.message_id)


@bot.message_handler(commands=['balance_default'])
def balance_default(message):
    global command_name
    command_name = 'balance_default'

    x = check_database(message.chat.id, 8)

    if x == None:
        bot.send_message(message.chat.id, 'Enter a customer number.  (This step is only for initialization)')
    else:
        msg = bot.send_message(message.chat.id, 'Getting data...')
        response = balance_rechargeHistory('balance', message=message, cust_no=x)[0]

        if response != False:
            bot.edit_message_text(response, message.chat.id, msg.message_id)


def balance_rechargeHistory(type, **kwargs):
    message = kwargs.get('message', None)
    cust_no = kwargs.get('cust_no', None)

    if cust_no == None:
        cust_no = message.text

    if type == 'recharge':
        try:
            return (main.check_last_recharge(cust_no), None)
        except:
            return False
    else:
        try:
            return main.check_balance(cust_no)
        except:
            return False


def check_database(ID, type):
    con = sqlite3.connect('data.db')
    db = con.cursor()

    x = db.execute(f'SELECT * FROM user_data WHERE id = {ID}; ')

    for row in x:
        if row[0] == ID and row[type] == 1:
            return row[2]
        else:
            return None

    con.close()


def notifier():

    con = sqlite3.connect('data.db')
    db = con.cursor()

    t = ['notify', 'notify_daily']
    for i in t:
        x = db.execute(f'SELECT * FROM user_data WHERE {i}=1')
    
        cust_nos = []
        chat_ids = []
        for row in x:
            cust_nos.append(row[2])
            chat_ids.append(row[0])


        for j in range(len(chat_ids)):
            if len(chat_ids) > 0:
                response = balance_rechargeHistory('balance', cust_no=cust_nos[j])

                if i == 'notify' and float(response[1]) < 100: 
                    bot.send_message(chat_ids[j], response)
                elif i == 'notify_daily':
                    bot.send_message(chat_ids[j], response)




@bot.message_handler()
def echo(message):
    if command_name == 'balance' or command_name == 'recharge':

        msg = bot.send_message(message.chat.id, 'Getting data...')
        response = balance_rechargeHistory(command_name, message=message)[0]

        if response != False:
            bot.edit_message_text(response, message.chat.id, msg.message_id)
            # bot.send_message(message.chat.id, response)
        else:
            bot.edit_message_text('Enter a valid customer number, or try again.', message.chat.id, msg.message_id)


    if command_name == 'notify':

        m = message.chat

        con = sqlite3.connect('data.db')
        db = con.cursor()

        try:
            db.execute(f'''INSERT INTO user_data (id, username, customer_id, first_name, last_name, notify) 
                        VALUES ({m.id}, '{m.username}', '{message.text}', '{m.first_name}', '{m.last_name}', 1)''')
        except sqlite3.IntegrityError:
            db.execute(f'UPDATE user_data SET notify=1 WHERE id={m.id}')

        con.commit()
        con.close()
        bot.send_message(message.chat.id, 'Setup success! You will get a message if remaining balance is less than ৳ 100.')
    

    if command_name == 'notify_daily':

        m = message.chat

        con = sqlite3.connect('data.db')
        db = con.cursor()

        try:
            db.execute(f'''INSERT INTO user_data (id, username, customer_id, first_name, last_name, notify) 
                        VALUES ({m.id}, '{m.username}', '{message.text}', '{m.first_name}', '{m.last_name}', 1)''')
        except sqlite3.IntegrityError:
            db.execute(f'UPDATE user_data SET notify_daily=1 WHERE id={m.id}')
            db.execute(f'UPDATE user_data SET customer_id={message.text} WHERE id={m.id}')

        con.commit()
        con.close()
        bot.send_message(message.chat.id, 'Setup success! You will get a message eveyday at 12:00 AM.')


    if command_name == 'last_recharge_default':

        m = message.chat

        con = sqlite3.connect('data.db')
        db = con.cursor()

        try:
            db.execute(f'''INSERT INTO user_data (id, username, customer_id, first_name, last_name, notify) 
                        VALUES ({m.id}, '{m.username}', '{message.text}', '{m.first_name}', '{m.last_name}', 1)''')
        except sqlite3.IntegrityError:
            db.execute(f'UPDATE user_data SET default_recharge=1 WHERE id={m.id}')
            db.execute(f'UPDATE user_data SET customer_id={message.text} WHERE id={m.id}')
        con.commit()
        con.close()
        bot.send_message(message.chat.id, '''Setup success! Just send the command next time to see last recharge history without entering customer no.''')


    if command_name == 'balance_default':

        m = message.chat

        con = sqlite3.connect('data.db')
        db = con.cursor()

        try:
            db.execute(f'''INSERT INTO user_data (id, username, customer_id, first_name, last_name, notify) 
                        VALUES ({m.id}, '{m.username}', '{message.text}', '{m.first_name}', '{m.last_name}', 1)''')
        except sqlite3.IntegrityError:
            db.execute(f'UPDATE user_data SET default_balance=1 WHERE id={m.id}')
            db.execute(f'UPDATE user_data SET customer_id={message.text} WHERE id={m.id}')

        con.commit()
        con.close()
        bot.send_message(message.chat.id, 'Just send the command /balance_default next time to see balance without entering customer no.')

def notifier_time(): 
    while True:
        if datetime.datetime.now().hour == 00 and datetime.datetime.now().minute > 30:
            notifier(3600)
        # time.sleep(3600)

# bot.polling()

botthread = threading.Thread(target=bot.polling)
botthread.start()
    
notifierthread = threading.Thread(target=notifier_time)
notifierthread.start()