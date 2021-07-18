from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions

url = 'https://prepaid.nesco.gov.bd'
cust_no = '71050717'


def build_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    return webdriver.Chrome(executable_path='./chromedriver.exe')
    

### Sending input and getting result page
def get_page(cust_no):

    browser = build_browser()
    browser.get(url)
    cust_id_input = browser.find_element_by_id('cust_no')

    cust_id_input.clear()
    cust_id_input.send_keys(cust_no)
    cust_id_input.send_keys(Keys.RETURN)

    result_page_source = browser.find_element_by_xpath("//html").get_attribute('outerHTML')

    browser.quit()

    return result_page_source


### Parsing balance and customer name
def get_name(soup):
    panel_body = soup.findAll(True, {'class': 'panel panel-primary'})
    name = panel_body[1].select_one('input[class*="form-control"]')['value']

    return name

def get_balance(soup):
    remaining_balance = soup.select_one('input[style*="bold"]')['value']

    return remaining_balance

def get_time(soup):
    updated_on = soup.select_one('small[style*="red"]').text
    updated_on = updated_on.replace('(Time: ', '').replace(')', '').replace(':00 ', '')

    return updated_on

    
### Parsing last payment info


def check_balance():
    soup = BeautifulSoup(get_page(cust_no), 'lxml')
    return f'''
	Customer no. : {cust_no}
	Customer name: {get_name(soup)}\n

	Remaining balance: ৳ {get_balance(soup)}
	Updated on: {get_time(soup)}
	'''

def get_last_recharge(soup):
    table_rows = soup.findAll('tr')

    data = []
    for table_cell in table_rows[1]:
    	data.append(table_cell.text)

    return {
			'token': data[2],
			'enammount': data[8],
			'reammount': data[9],
			'unit': data[10], 
			'method': data[11],
			'date': data[12],
			'remote': data[13],
    }

def check_last_recharge():
	soup = BeautifulSoup(get_page(cust_no), 'lxml')
	x = get_last_recharge(soup)
	return f'''
	Customer no. : {cust_no}
	Customer name: {get_name(soup)}\n

	Date: {x['date']}
	Recharge ammount: ৳ {x['reammount']}
	Energy ammount: ৳ {x['enammount']}
	Unit (kWh): {x['unit']}
	Payment method: {x['method']}
	Remote payment: {x['remote']}
	'''

print(check_last_recharge())