import telebot
import os
from threading import Thread
from dotenv import load_dotenv
from datetime import datetime
from time import sleep

import data_collector 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


creds = credentials.Certificate('toy-bank-bot-firebase-adminsdk.json')
firebase_admin.initialize_app(creds)
db = firestore.client()
users = db.collection(u'users')


load_dotenv()
API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY, parse_mode='HTML')

command_name = None
starting_message = "/balance - Check current balance\n/balance_default - Check current balance with preset customer no.\n/last_recharge - Check last recharge details\n/last_recharge_default - Check last recharge details with preset customer no.\n/notify - Get balance update if balance is less than ৳100\n/notify_daily - Get balance update daily at 06:00 AM"


def message_formatter(type: str, cust_no) -> str:
    """Gets data from data_collector.py and formats message for sending to TG"""
    
    if type == 'balance':
        try:
            info = data_collector.check_balance(cust_no)

            message = f'''
                <b><u>Balance info</u></b>
    Customer no.:       <b>{info['cust_no']}</b>
    Customer name:  <b>{info['cust_name']}</b>
        
    Remaining balance:   <b>৳{info['balance']}</b>
    Updated on:   <b>{info['time']}</b>'''

            return message
        
        except:
            return False

    elif type == 'recharge':
        try:
            info = data_collector.check_last_recharge(cust_no)

            message = f'''
                <b><u>Last recharge info</u></b>
    Customer no.:       <b>{info['cust_no']}</b>
    Customer name:  <b>{info['cust_name']}</b>
    
    Date:   <b>{info['info']['date']}</b>
    Recharge amount:   <b>৳{info['info']['re_amount']}</b>
    Energy amount:        <b>৳{info['info']['en_amount']}</b>
    Unit (kWh):                  <b>{info['info']['unit']}</b>
    Payment method:     <b>{info['info']['method']}</b>
    Remote payment:     <b>{info['info']['remote']}</b>
    Token: <b>{info['info']['token']}</b>'''

            return message
        
        except:
            return False

    elif type == 'low_balance':
        try:
            info = data_collector.check_balance(cust_no)

            message = f'''
        <b><u>LOW BALANCE</u></b>
    Customer no.:       <b>{info['cust_no']}</b>
    Customer name:  <b>{info['cust_name']}</b>
        
    Remaining balance:   <b>৳{info['balance']}</b>
    Updated on:   <b>{info['time']}</b>'''

            return message
        
        except:
            return False



def doc_exists(doc_id: str, doc_name='users'):
    """Checks if a document in Firestore exists or not."""

    doc_ref = db.collection(doc_name).document(doc_id)

    doc = doc_ref.get()
  
    if doc.exists:
        return True
    else:
        return False
    

def get_cust_nos(doc_id: str, field: str) -> list:
    """Gets preset customer nos from Firestore."""
    
    if doc_exists(doc_id):
        doc_ref = users.document(doc_id)

        try:
            cust_nos = doc_ref.get().to_dict()[field]
            return cust_nos
        except:
            return None

    else:
        return None 


def create_doc(chat: dict):
    """Creates a Firestore document from a TG message.chat object"""

    user_data = {
        'tg_id': str(chat.id), 
        'username': chat.username, 
        'name': chat.first_name + ' ' + chat.last_name, 
        'presets': None, 
        'notify': None, 
        'notify_daily': None}
    
    tg_id = str(chat.id)
    doc_ref = users.document(tg_id)

    doc_ref.set(user_data)


def set_cust_no(doc_id: str, field: str, cust_no: str):
    
    doc_ref = users.document(doc_id)
    doc_ref.update({field: firestore.ArrayUnion([cust_no])})


@bot.message_handler(commands=['start', 'help'])
def start(message):
    global command_name
    command_name = 'start'
    bot.send_message(message.chat.id, starting_message)


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
def notify_daily(message):
    global command_name
    command_name = 'notify_daily'
    bot.send_message(message.chat.id, 'Enter a customer number.')


@bot.message_handler(commands=['last_recharge_default'])
def last_rechrage_default(message):
    global command_name
    command_name = 'last_recharge_default'

    tg_id = str(message.chat.id)
    cust_nos = get_cust_nos(tg_id, 'presets')

    if cust_nos == None:
        bot.send_message(tg_id, 'Enter a customer number.  (This step is only for initialization)')
    
    else:
        cust_no = cust_nos[0]
        msg = bot.send_message(tg_id, 'Getting data...')
        response = message_formatter('recharge', cust_no)

        if response != False:
            bot.edit_message_text(response, tg_id, msg.message_id)
        else:
            bot.edit_message_text('Please try again.', tg_id, msg.message_id)


@bot.message_handler(commands=['balance_default'])
def balance_default(message):
    global command_name
    command_name = 'balance_default'

    tg_id = str(message.chat.id)
    cust_nos = get_cust_nos(tg_id, 'presets')

    if cust_nos == None:
        bot.send_message(tg_id, 'Enter a customer number.  (This step is only for initialization)')
    
    else:
        cust_no = cust_nos[0]
        msg = bot.send_message(tg_id, 'Getting data...')
        response = message_formatter('balance', cust_no)

        if response != False:
            bot.edit_message_text(response, tg_id, msg.message_id)
        else:
            bot.edit_message_text('Please try again.', tg_id, msg.message_id)


@bot.message_handler()
def echo(message):
    if command_name == 'start':
      bot.send_message(message.chat.id, starting_message)
    
    if command_name == 'balance' or command_name == 'recharge':

        msg = bot.send_message(message.chat.id, 'Getting data...')
        response = message_formatter(command_name, message.text)

        if response != False:
            bot.edit_message_text(response, message.chat.id, msg.message_id)
        else:
            bot.edit_message_text('Enter a valid customer number, or try again.', message.chat.id, msg.message_id)


    if command_name == 'notify':

        tg_id = str(message.chat.id)

        if not doc_exists(tg_id):
            create_doc(message.chat)

        if doc_exists(tg_id):
            set_cust_no(tg_id, 'notify', message.text)

        bot.send_message(message.chat.id, 'Setup success! You will get a message if remaining balance balance is less than ৳100.')
    

    if command_name == 'notify_daily':

        tg_id = str(message.chat.id)

        if not doc_exists(tg_id):
            create_doc(message.chat)

        if doc_exists(tg_id):
            set_cust_no(tg_id, 'notify_daily', message.text)

        bot.send_message(message.chat.id, 'Setup success! You will get a balance update eveyday at 06:00 AM.')


    if command_name == 'last_recharge_default':

        tg_id = str(message.chat.id)

        if not doc_exists(tg_id):
            create_doc(message.chat)

        if doc_exists(tg_id):
            set_cust_no(tg_id, 'presets', message.text)

        bot.send_message(message.chat.id, "Setup success! Just send the command /last_recharge_default next time to see last recharge history without entering customer no.")


    if command_name == 'balance_default':

        tg_id = str(message.chat.id)

        if not doc_exists(tg_id):
            create_doc(message.chat)

        if doc_exists(tg_id):
            set_cust_no(tg_id, 'presets', message.text)

        bot.send_message(message.chat.id, 'Just send the command /balance_default next time to see balance without entering customer no.')


def notifier():

    sent_notify_to: list[str] = []

    docs_notify = users.where('notify', u'!=', 'null').stream()
    for doc in docs_notify:
        cust_no = doc.to_dict()['notify'][0]
        tg_id = doc.to_dict()['tg_id']

        balance = data_collector.get_balance(cust_no=cust_no)

        if float(balance) < 100: 
            response = message_formatter('low_balance', cust_no)
            bot.send_message(tg_id, response)
        
        sent_notify_to.append((cust_no, tg_id))


    docs_notify_daily = users.where('notify_daily', '!=', 'null').stream()
    for doc in docs_notify_daily:
        cust_no = doc.to_dict()['notify_daily'][0]
        tg_id = doc.to_dict()['tg_id']

        if (cust_no, tg_id) not in sent_notify_to:
            response = message_formatter('balance', cust_no)
            bot.send_message(tg_id, response)


def notifier_time():
    while True:
        if datetime.now().hour == 00 and datetime.now().minute > 00:
            notifier()
            sleep(3600)
        else:
            sleep(1800)


bot_thread = Thread(target=bot.polling)
bot_thread.start()

notifier_thread = Thread(target=notifier_time)
notifier_thread.start()