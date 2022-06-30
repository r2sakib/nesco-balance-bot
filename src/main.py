# Python version = 3.10.4

import os
from threading import Thread
from dotenv import load_dotenv
from datetime import datetime
from time import sleep
import traceback

from telebot import TeleBot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import schedule

import data_collector 

creds = credentials.Certificate('src/firebase-admin-sdk.json')
firebase_admin.initialize_app(creds)
db = firestore.client()
users = db.collection(u'users')


load_dotenv()
TG_BOT_TOKEN = os.environ['TG_BOT_TOKEN']
bot = TeleBot(TG_BOT_TOKEN, parse_mode='HTML')

command_name = None
starting_message = ("/balance - Check current balance\n"
                    "/balance_default - Check current balance with preset customer no.\n"
                    "/last_recharge - Check last recharge details\n"
                    "/last_recharge_default - Check last recharge details with preset customer no.\n"
                    "/notify - Get balance update if balance is less than ৳100\n"
                    "/notify_daily - Get balance update daily at 06:00 AM\n"
                    )


def logger(log):
    with open('logs.md', 'a') as log_file:
        timestamp = datetime.now()
        log_file.write(f'\n\n{timestamp}\n\n```{log}```\n\n---')


def message_formatter(type: str, cust_no) -> str:
    """Gets data from data_collector.py and formats message for sending to TG"""
    
    if type == 'balance':
        try:
            info = data_collector.check_balance(cust_no)

            message = (f"<b><u>Balance info</u></b>\n"
                        f"  Customer no.:       <b>{info['cust_no']}</b>\n"
                        f"  Customer name:  <b>{info['cust_name']}</b>\n\n"
                            
                        f"  Remaining balance: <b>৳{info['balance']}</b>\n"
                        f"  Updated on: <b>{info['time']}</b>\n"
                        )

            return message
        
        except:
            return False

    elif type == 'recharge':
        try:
            info = data_collector.check_last_recharge(cust_no)

            message = (f"<b><u>Last recharge info</u></b>\n"
                        f"  Customer no.:       <b>{info['cust_no']}</b>\n"
                        f"  Customer name:  <b>{info['cust_name']}</b>\n\n"
                        
                        f"  Date: <b>{info['info']['date']}</b>\n"
                        f"  Recharge amount:   <b>৳{info['info']['re_amount']}</b>\n"
                        f"  Energy amount:        <b>৳{info['info']['en_amount']}</b>\n"
                        f"  Unit (kWh):                  <b>{info['info']['unit']}</b>\n"
                        f"  Payment method:     <b>{info['info']['method']}</b>\n"
                        f"  Remote payment:     <b>{info['info']['remote']}</b>\n"
                        f"  Token: <b>{info['info']['token']}</b>\n"
                        )

            return message
        
        except:
            return False

    elif type == 'low_balance':
        try:
            info = data_collector.check_balance(cust_no)

            message = (f"<b><u>LOW BALANCE</u></b>\n"
                        f"  Customer no.:       <b>{info['cust_no']}</b>\n"
                        f"  Customer name:  <b>{info['cust_name']}</b>\n\n"
                            
                        f"  Remaining balance:   <b>৳{info['balance']}</b>\n"
                        f"  Updated on:   <b>{info['time']}</b>\n"
                        )

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
def start_help(message):
    try:
        global command_name
        command_name = 'start'
        bot.send_message(message.chat.id, starting_message, parse_mode=None)

    except Exception:
        logger(traceback.format_exc())

@bot.message_handler(commands=['balance'])
def balance(message):
    try:
        global command_name
        command_name = 'balance'
        bot.send_message(message.chat.id, 'Enter a customer number.')

    except Exception:
        logger(traceback.format_exc())


@bot.message_handler(commands=['last_recharge'])
def recharge(message):
    try:
        global command_name
        command_name = 'recharge'
        bot.send_message(message.chat.id, 'Enter a customer number.')

    except Exception:
        logger(traceback.format_exc())

@bot.message_handler(commands=['notify'])
def notify(message):
    try:
        global command_name
        command_name = 'notify'
        bot.send_message(message.chat.id, 'Enter a customer number.')

    except Exception:
        logger(traceback.format_exc())

@bot.message_handler(commands=['notify_daily'])
def notify_daily(message):
    try:
        global command_name
        command_name = 'notify_daily'
        bot.send_message(message.chat.id, 'Enter a customer number.')

    except Exception:
        logger(traceback.format_exc())


@bot.message_handler(commands=['last_recharge_default'])
def last_rechrage_default(message):
    try:
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

    except Exception:
        logger(traceback.format_exc())
        try:
            bot.send_message('Error occured. Try again after some time.', tg_id)
        except Exception:
            logger(traceback.format_exc())



@bot.message_handler(commands=['balance_default'])
def balance_default(message):
    try:
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

    except Exception:
        logger(traceback.format_exc())
        try:
            bot.send_message('Error occured. Try again after some time.', tg_id)
        except Exception:
            logger(traceback.format_exc())


@bot.message_handler()
def handle_all_messages(message):
    try:
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

    except Exception:
        logger(traceback.format_exc())
        try:
            bot.send_message('Error occured. Try again after some time.', tg_id)
        except Exception:
            logger(traceback.format_exc())


def notifier():

    try:
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
    
    except Exception:
        logger(traceback.format_exc())


def notifier_time():
    schedule.every().day.at("00:00").do(notifier)

    while True:
        schedule.run_pending()
        sleep(60)
try:
    bot_thread = Thread(target=bot.polling)
    bot_thread.start()

    notifier_thread = Thread(target=notifier_time)
    notifier_thread.start()

except Exception:
    logger(traceback.format_exc())