# Python version = 3.10.4

import os
from threading import Thread
from dotenv import load_dotenv
from time import sleep
import traceback

from telebot import TeleBot, types
import schedule

import data_collector 
from funcs import *


"""Initilized Firebase on ./funcs.py"""

load_dotenv()
TG_BOT_TOKEN = os.environ['TG_BOT_TOKEN']
bot = TeleBot(TG_BOT_TOKEN, parse_mode='HTML')

command_name = None
STARTING_MESSAGE = ("/balance - Check current balance\n"
                    "/recharge_details - Check last recharge details.\n"
                    "/presets - Add customer numbers for easy access\n"
                    "/notify - Get balance update if balance is less than ৳100\n"
                    "/notify_daily - Get balance update daily at 06:00 AM\n"
                    )

SELECTION_MESSAGE = '• Enter a customer number.\n\n• Or select one from below. (Will be shown below if you have added persets.)'


@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    try:
        global command_name
        command_name = 'start'
        bot.send_message(message.chat.id, STARTING_MESSAGE, parse_mode=None)

    except Exception:
        logger(traceback.format_exc())


@bot.message_handler(commands=['balance'])
def balance(message):
    try:
        global command_name
        command_name = 'balance'

        tg_id = message.chat.id
        if doc_exists(tg_id):
            bot.send_message(tg_id, SELECTION_MESSAGE, reply_markup=generate_reply_markup(tg_id, 'reply_keyboard'))
        
        else:
            bot.send_message(tg_id, SELECTION_MESSAGE)

    except Exception:
        logger(traceback.format_exc())


@bot.message_handler(commands=['recharge_details'])
def recharge_details(message):
    try:
        global command_name
        command_name = 'recharge_details'

        tg_id = message.chat.id
        if doc_exists(tg_id):
            bot.send_message(tg_id, SELECTION_MESSAGE, reply_markup=generate_reply_markup(tg_id, 'reply_keyboard'))
        
        else:
            bot.send_message(tg_id, SELECTION_MESSAGE)

    except Exception:
        logger(traceback.format_exc())


@bot.message_handler(commands=['notify'])
def notify(message):
    try:
        global command_name
        command_name = 'notify'

        tg_id: int = message.chat.id

        if doc_exists(tg_id):
            cust_nos: list = get_cust_nos(tg_id, 'notify')

            if len(cust_nos) == 0:
                bot.send_message(tg_id, SELECTION_MESSAGE, reply_markup=generate_reply_markup(tg_id, 'reply_keyboard', cust_nos=cust_nos))

            elif len(cust_nos) > 0:
                inline_markup = types.InlineKeyboardMarkup(row_width=2)
                btn_add= types.InlineKeyboardButton('Add', callback_data='Add')
                btn_remove = types.InlineKeyboardButton('Remove', callback_data='Remove')

                inline_markup.add(btn_add, btn_remove)

                msg = bot.send_message(tg_id, ('• Tap on <b>Add</b> if you want to add <i>low balance update</i> for another customer no.\n\n'
                                        '• Tap on <b>Remove</b> to remove a customer number from <i>low balance update</i>.'), reply_markup=inline_markup)

                global message_id, chat_id
                message_id = msg.id
                chat_id = tg_id
        else:
            bot.send_message(tg_id, SELECTION_MESSAGE)

    except Exception:
        logger(traceback.format_exc())


@bot.message_handler(commands=['notify_daily'])
def notify_daily(message):
    try:
        global command_name
        command_name = 'notify_daily'

        tg_id: int = message.chat.id

        if doc_exists(tg_id):
            cust_nos: list = get_cust_nos(tg_id, 'notify_daily')

            if len(cust_nos) == 0:
                bot.send_message(tg_id, SELECTION_MESSAGE, reply_markup=generate_reply_markup(tg_id, 'reply_keyboard', cust_nos=cust_nos))

            elif len(cust_nos) > 0:
                inline_markup = types.InlineKeyboardMarkup(row_width=2)
                btn_add= types.InlineKeyboardButton('Add', callback_data='Add')
                btn_remove = types.InlineKeyboardButton('Remove', callback_data='Remove')

                inline_markup.add(btn_add, btn_remove)

                msg = bot.send_message(tg_id, ('• Tap on <b>Add</b> if you want to add <i>daily balance update</i> for another customer no.\n\n'
                                        '• Tap on <b>Remove</b> to remove a customer number from <i>daily balance update</i>.'), reply_markup=inline_markup)

                global message_id, chat_id
                message_id = msg.id
                chat_id = tg_id
        
        else:
            bot.send_message(tg_id, SELECTION_MESSAGE)

    except Exception:
        logger(traceback.format_exc())



@bot.message_handler(commands=['presets'])
def presets(message):
    try:
        global command_name
        command_name = 'presets'

        tg_id: int = message.chat.id

        if doc_exists(tg_id):
            cust_nos: list = get_cust_nos(tg_id, 'presets')

            if len(cust_nos) == 0:
                bot.send_message(tg_id, 'Enter a customer no. to add to <i>presets</i>.', reply_markup=generate_reply_markup(tg_id, 'reply_keyboard', cust_nos=cust_nos))

            elif len(cust_nos) > 0:
                inline_markup = types.InlineKeyboardMarkup(row_width=2)
                btn_add= types.InlineKeyboardButton('Add', callback_data='Add')
                btn_remove = types.InlineKeyboardButton('Remove', callback_data='Remove')

                inline_markup.add(btn_add, btn_remove)

                msg = bot.send_message(tg_id, ('• Tap on <b>Add</b> if you want to add a customer number to <i>presets</i>.\n\n'
                                        '• Tap on <b>Remove</b> to remove a customer number from <i>presets</i>.'), reply_markup=inline_markup)

                global message_id, chat_id
                message_id = msg.id
                chat_id = tg_id
        
        else:
            bot.send_message(tg_id, 'Enter a customer no. to add to <i>presets</i>.')


    except Exception:
        logger(traceback.format_exc())
        try:
            bot.send_message(tg_id, 'Error occured. Try again after some time.')
        except Exception:
            logger(traceback.format_exc())


query_data = 'Add'
query_data_2 = 'Add'
query_data_3 = 'Add'

@bot.callback_query_handler(func=lambda call: True)
def process_callbacks(query):

    if command_name == 'notify' and query.data == 'Add':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, SELECTION_MESSAGE,
                            reply_markup=generate_reply_markup(chat_id, 'reply_keyboard', field='presets'))

    elif command_name == 'notify' and query.data == 'Remove':
        bot.edit_message_text('Select one from below <b>to remove</b> from <i>low balance update</i>.',
                                chat_id, message_id, reply_markup=generate_reply_markup(chat_id, 'inline_keyboard', field='notify'))

        return

    if command_name == 'notify_daily' and query.data == 'Add':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, SELECTION_MESSAGE, 
                        reply_markup=generate_reply_markup(chat_id, 'reply_keyboard', field='presets'))

    elif command_name == 'notify_daily' and query.data == 'Remove':
        bot.edit_message_text('Select one from below <b>to remove</b> from <i>daily balance update</i>.',
                                chat_id, message_id, reply_markup=generate_reply_markup(chat_id, 'inline_keyboard', field='notify_daily'))

        return

    if command_name == 'presets' and query.data == 'Add':
        bot.edit_message_text('Enter a customer no. to add to <i>presets</i>.', chat_id, message_id)

    elif command_name == 'presets' and query.data == 'Remove':
        bot.edit_message_text('Select one from below <b>to remove</b> from <i>presets</i>.',
                                chat_id, message_id, reply_markup=generate_reply_markup(chat_id, 'inline_keyboard', field='presets'))
    

    if command_name == 'notify':
        try:
            cust_no = int(query.data)
            remove_cust_no(chat_id, 'notify', query.data)
            bot.edit_message_text(f'Customer no.: <b>{cust_no}</b> removed from <i>low balance update</i>.', chat_id, message_id)

        except:
            global query_data; query_data = query.data

    elif command_name == 'notify_daily':
        try:
            cust_no = int(query.data)
            remove_cust_no(chat_id, 'notify_daily', query.data)
            bot.edit_message_text(f'Customer no.: <b>{cust_no}</b> removed from <i>daily balance update</i>.', chat_id, message_id)

        except:
            global query_data_2; query_data_2 = query.data

    elif command_name == 'presets':
        try:
            cust_no = int(query.data)
            remove_cust_no(chat_id, 'presets', query.data)
            bot.edit_message_text(f'Customer no.: <b>{cust_no}</b> removed from <i>presets.</i>.', chat_id, message_id)

        except:
            global query_data_3; query_data_3 = query.data



@bot.message_handler()
def handle_all_messages(message):
    try:
        tg_id = str(message.chat.id)
        remove_keyboard = types.ReplyKeyboardRemove()

        if check_input_validity(message.text) == True:

            if command_name == 'start':
                bot.send_message(message.chat.id, STARTING_MESSAGE)
            

            if command_name == 'balance' or command_name == 'recharge_details':

                msg = bot.send_message(message.chat.id, 'Getting data...', reply_markup=remove_keyboard)
                response = message_formatter(command_name, message.text)

                if response != False:
                    bot.delete_message(tg_id, msg.id)
                    bot.send_message(message.chat.id, response, reply_markup=remove_keyboard)
                else:
                    bot.edit_message_text('Enter a valid customer number, or try again.', message.chat.id, msg.message_id)


            if command_name == 'notify':

                if query_data == 'Add':
                    
                    if not doc_exists(tg_id):
                        create_doc(message.chat)

                    set_cust_no(tg_id, 'notify', message.text)

                    bot.send_message(message.chat.id, f'Setup success!\nYou will get a message if remaining balance is less than ৳100, for customer no.: <b>{message.text}</b>',
                                    reply_markup=remove_keyboard)
            

            if command_name == 'notify_daily':

                if query_data_2 == 'Add':
                    
                    if not doc_exists(tg_id):
                        create_doc(message.chat)

                    set_cust_no(tg_id, 'notify_daily', message.text)

                    bot.send_message(message.chat.id, f'Setup success!\nYou will get a balance update eveyday at 06:00 AM for customer no.: <b>{message.text}</b>',
                                    reply_markup=remove_keyboard)


            if command_name == 'presets':

                if query_data_3 == 'Add':
                    
                    if not doc_exists(tg_id):
                        create_doc(message.chat)

                    set_cust_no(tg_id, 'presets', message.text)

                    bot.send_message(tg_id, f"Customer number: <b>{message.text}</b> added to presers.!\n\nJust send the command /balance\nor /recharge_details next time to see balance or last recharge details without entering customer no.\n\nYou can add more presets too.")

        else:
            bot.send_message(message.chat.id, 'Input not valid. Enter again.')

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
            
            tg_id = doc.to_dict()['tg_id']
            cust_nos = doc.to_dict()['notify']

            for cust_no in cust_nos:

                balance = data_collector.get_balance(cust_no=cust_no)

                if float(balance) < 100: 
                    response = message_formatter('low_balance', cust_no)
                    bot.send_message(tg_id, response)

                    sent_notify_to.append((cust_no, tg_id))


        docs_notify_daily = users.where('notify_daily', '!=', 'null').stream()
        for doc in docs_notify_daily:

            tg_id = doc.to_dict()['tg_id']
            cust_nos = doc.to_dict()['notify_daily']

            for cust_no in cust_nos:
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
