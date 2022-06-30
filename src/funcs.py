# Python version = 3.10.4

from datetime import datetime

from telebot import types
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import data_collector 


creds = credentials.Certificate('src/.firebase-admin-sdk.json')
firebase_admin.initialize_app(creds)
db = firestore.client()
users = db.collection(u'users')


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

    elif type == 'recharge_details':
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


def doc_exists(doc_id: str | int, doc_name='users'):
    """Checks if a document in Firestore exists or not."""

    doc_id = str(doc_id)

    doc_ref = db.collection(doc_name).document(doc_id)

    doc = doc_ref.get()
  
    if doc.exists:
        return True
    else:
        return False
    

def create_doc(chat: dict):
    """Creates a Firestore document from a TG message.chat object"""

    user_data = {
        'tg_id': str(chat.id), 
        'username': chat.username, 
        'name': chat.first_name + ' ' + chat.last_name, 
        'presets': [], 
        'notify': [], 
        'notify_daily': []}
    
    tg_id = str(chat.id)
    doc_ref = users.document(tg_id)

    doc_ref.set(user_data)


def set_cust_no(doc_id: str, field: str, cust_no: str | int):

    doc_id = str(doc_id)
    
    doc_ref = users.document(doc_id)
    doc_ref.update({field: firestore.ArrayUnion([cust_no])})


def remove_cust_no(doc_id: str, field: str, cust_no: str):

    doc_id = str(doc_id)

    doc_ref = users.document(doc_id)
    doc_ref.update({field: firestore.ArrayRemove([cust_no])})


def get_cust_nos(doc_id: str | int, field: str) -> list:
    """Gets preset customer nos from Firestore. provided a doc_id (TG chat id)"""
    
    doc_id = str(doc_id)

    if doc_exists(doc_id):
        doc_ref = users.document(doc_id)

        try:
            cust_nos = doc_ref.get().to_dict()[field]
            return cust_nos
        except:
            return None

    else:
        return None 


def generate_reply_markup(tg_id: str | int, type: str, cust_nos: list = None, field: str = 'presets'):
    """Generates Telebot ReplyKeyboardMarkup (reply_keyboard) | InlineKeyboardMarkup (inline_keyboard)
    of customer numbers from Firestore using tg_id (doc_id)
    """

    cust_nos = get_cust_nos(tg_id, field)

    if type == 'reply_keyboard':
        reply_markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)

        buttons = []
        for cust_no in cust_nos:
            buttons.append(types.KeyboardButton(cust_no))

        reply_markup.add(*buttons)
    

    elif type == 'inline_keyboard':
        reply_markup = types.InlineKeyboardMarkup(row_width=2)

        buttons = []
        for cust_no in cust_nos:
            buttons.append(types.InlineKeyboardButton(cust_no, callback_data=cust_no))

        reply_markup.add(*buttons)

    return reply_markup


def check_input_validity(text: str):
    try:
        text = int(text)
        return True
    except:
        False