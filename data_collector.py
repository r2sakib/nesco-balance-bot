from bs4 import BeautifulSoup
import mechanize
from typing import Union
    

### Sending input and getting result page
def get_page(cust_no):

    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)

    response = br.open("http://prepaid.nesco.gov.bd/")
    br.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'), ('Accept', '*/*')]

    br.select_form(id='customer-form')
    br['cust_no'] = str(cust_no)

    response = br.submit()

    return response


### Parsing balance and customer name
def get_name(soup):
    panel_body = soup.findAll(True, {'class': 'panel panel-primary'})
    name = panel_body[1].select_one('input[class*="form-control"]')['value']

    return name

<<<<<<< HEAD
def get_balance(soup) -> str:
    remaining_balance = soup.select_one('input[style*="bold"]')['value']
=======
def get_balance(soup=None, cust_no=None) -> str:
    if soup == None:
        soup = BeautifulSoup(get_page(cust_no), 'lxml')
>>>>>>> dev

    remaining_balance = soup.select_one('input[style*="bold"]')['value']
    return remaining_balance


def get_time(soup):
    updated_on = soup.select_one('small[style*="black"]').teinfo['info']
    updated_on = updated_on.replace('(সময়ঃ ', '').replace(')', '').replace(':00 ', '')

    return updated_on

    
### Parsing last payment info

def get_last_recharge(soup):
	table_rows = soup.findAll('tr')

	data = []
	for table_cell in table_rows[1]:
<<<<<<< HEAD
		data.append(table_cell.teinfo['info'])
=======
		data.append(table_cell.text)
>>>>>>> dev

	return {
			'token': data[0],
			'en_amount': data[7],
			're_amount': data[8],
			'unit': data[9], 
			'method': data[10],
			'date': data[11],
			'remote': data[12],
    }


### Genereting outputs
def check_balance(cust_no: Union[int, str]) -> dict:

    soup = BeautifulSoup(get_page(cust_no), 'lxml')
<<<<<<< HEAD
    b = get_balance(soup)

    cust_name = get_name(soup)
    if cust_name == 'MOST. ZESMIN ARA KHATUN':
        cust_name = 'JESMIN ARA'
    
    return f'''
    <b><u>Balance info</u></b>
  Customer no.:       <b>{cust_no}</b>
  Customer name:  <b>{cust_name}</b>
    
  Remaining balance:   <b>৳{b}</b>
  Updated on:   <b>{get_time(soup)}</b>
	''', b
=======
    balance = get_balance(soup=soup)

    cust_name = get_name(soup)
    if cust_name == 'MOST. ZESMIN ARA KHATUN':
        cust_name = 'JESMIN ARA'
    
    time = get_time(soup)

    return {
        'cust_no': cust_no,
        'cust_name': cust_name,
        'time': time,
        'balance': balance,
    }


def check_last_recharge(cust_no: Union[int, str]) -> dict:
>>>>>>> dev

	soup = BeautifulSoup(get_page(cust_no), 'lxml')
<<<<<<< HEAD
	x = get_last_recharge(soup)
	token = x['token']
	token = token.replace('\n\n\t\t\t\t\t\t\t\t\t\t\t', '')
	token = token.replace('\n', '')
=======
	recharge_info = get_last_recharge(soup)
	token = recharge_info['token']
	token = token.replace('\n\n\t\t\t\t\t\t\t\t\t\t\t', '').replace('\n', '')
	recharge_info['token'] = token
>>>>>>> dev

	cust_name = get_name(soup)
	if cust_name == 'MOST. ZESMIN ARA KHATUN':
		cust_name = 'JESMIN ARA'
<<<<<<< HEAD

	return f'''
    <b><u>Last recharge info</u></b>
  Customer no.:       <b>{cust_no}</b>
  Customer name:  <b>{cust_name}</b>
  
  Date:   <b>{x['date']}</b>
  Recharge amount:   <b>৳{x['reamount']}</b>
  Energy amount:        <b>৳{x['enamount']}</b>
  Unit (kWh):                 <b>{x['unit']}</b>
  Payment method:     <b>{x['method']}</b>
  Remote payment:     <b>{x['remote']}</b>
  Token: <b>{token}</b>
	'''
=======
        
	return {
        'cust_no': cust_no,
        'cust_name': cust_name,
        'info': recharge_info}
>>>>>>> dev
