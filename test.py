import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


creds = credentials.Certificate('toy-bank-bot-firebase-adminsdk.json')
app = firebase_admin.initialize_app(creds)
db = firestore.client()
users = db.collection(u'users')



msg = {'id': 1424161160, 'type': 'private', 'title': None, 'username': 'anakinnn', 'first_name': 'Anakin', 'last_name': 'Skywalker'}
cust_no = '71050717'

doc_ref = users.document(str(msg['id']))

def doc_exists(doc_id: str, doc_name='users'):
    doc_ref = db.collection(doc_name).document(doc_id)

    doc = doc_ref.get()
  
    if doc.exists:
        return True
    else:
        return False

# if doc_exists(str(msg['id'])):
#     doc_ref.update({
#         'notify': [cust_no, '71050716']
#     })

# else:
#     doc_ref.set({
#         'id': msg['id'],
#         'username': msg['username'],
#         'name': msg['first_name'] + ' ' + msg['last_name'],
#         'balance_presets': [cust_no],
#         'recharge_presets': [cust_no],}
#     )

docs = users.where('notify', u'!=', 'null').stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
