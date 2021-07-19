from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

url = 'https://prepaid.nesco.gov.bd'


def build_browser():
    driver_exe = './chromedriver.exe'
    options = webdriver.ChromeOptions()
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(driver_exe, options=options)
    return driver
    

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

def get_last_recharge(soup):
    table_rows = soup.findAll('tr')

    data = []
    for table_cell in table_rows[1]:
    	data.append(table_cell.text)

    return {
			'token': data[1],
			'enamount': data[8],
			'reamount': data[9],
			'unit': data[10], 
			'method': data[11],
			'date': data[12],
			'remote': data[13],
    }


### Genereting outputs
def check_balance(cust_no):
    soup = BeautifulSoup(get_page(cust_no), 'lxml')
    b = get_balance(soup)
    return f'''
	Customer no. :       *{cust_no}*\nCustomer name:   *{get_name(soup)}*\n

	Remaining balance:   *৳ {b}*
	Updated on:   *{get_time(soup)}*
	''', b

def check_last_recharge(cust_no):
	soup = BeautifulSoup(get_page(cust_no), 'lxml')
	x = get_last_recharge(soup)
	return f'''
	Customer no. :       *{cust_no}*\nCustomer name:   *{get_name(soup)}*\n

	Date:   *{x['date']}*
	Recharge amount:    *৳ {x['reamount']}*
	Energy amount:         *৳ {x['enamount']}*
	Unit (kWh):                   *{x['unit']}*
	Payment method:     *{x['method']}*
	Remote payment:     *{x['remote']}*\nToken:   *{x['token']}*
	'''

# print(check_balance(71050717))