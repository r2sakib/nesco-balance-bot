from bs4 import BeautifulSoup
import mechanize
    

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

def get_balance(soup):
    remaining_balance = soup.select_one('input[style*="bold"]')['value']

    return remaining_balance

def get_time(soup):
    updated_on = soup.select_one('small[style*="black"]').text
    updated_on = updated_on.replace('(সময়ঃ ', '').replace(')', '').replace(':00 ', '')

    return updated_on

    
### Parsing last payment info

def get_last_recharge(soup):
    table_rows = soup.findAll('tr')

    data = []
    for table_cell in table_rows[1]:
    	data.append(table_cell.text)

    return {
			'token': data[0],
			'enamount': data[7],
			'reamount': data[8],
			'unit': data[9], 
			'method': data[10],
			'date': data[11],
			'remote': data[12],
    }


### Genereting outputs
def check_balance(cust_no):
    soup = BeautifulSoup(get_page(cust_no), 'lxml')
    b = get_balance(soup)
    return f'''
	Customer no. :       <b>{cust_no}</b>\nCustomer name:   <b>{get_name(soup)}</b>\n

	Remaining balance:   <b>৳{b}</b>
	Updated on:   <b>{get_time(soup)}</b>
	''', b

def check_last_recharge(cust_no):
	soup = BeautifulSoup(get_page(cust_no), 'lxml')
	x = get_last_recharge(soup)
	return f'''
	Customer no. :       <b>{cust_no}</b>\nCustomer name:   <b>{get_name(soup)}</b>\n

	Date:   <b>{x['date']}</b>
	Recharge amount:    <b>৳{x['reamount']}</b>
	Energy amount:         <b>৳{x['enamount']}</b>
	Unit (kWh):                   <b>{x['unit']}</b>
	Payment method:     <b>{x['method']}</b>
	Remote payment:     <b>{x['remote']}</b>\n Token:  *{x['token']}</b>
	'''