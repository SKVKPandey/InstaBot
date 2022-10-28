import os
import zipfile

from selenium import webdriver

# PROXY_HOST = '185.199.231.45'  # rotating proxy or host
# PROXY_PORT = 8382 # port
# PROXY_USER = 'ltssmxdz' # username
from seleniumwire import webdriver
import time


# replace 'user:pass@ip:port' with your information
options = {
	'proxy': {
		'http': 'http://cwnwshek:gyb1tqnz68g3@144.168.217.88:8780',
		'https': 'http://cwnwshek:gyb1tqnz68g3@144.168.217.88:8780',
		'no_proxy': 'localhost,127.0.0.1'
	}
}

# replace 'your_absolute_path' with your chrome binary's aboslute path
driver = webdriver.Chrome('WebDriver\chromedriver.exe', seleniumwire_options=options)

driver.get('https://www.instagram.com/')

time.sleep(20)

submit = driver.find_element("xpath", "//button[@tabindex='0']").click()

time.sleep(10)

driver.quit()

# <button class="_a9-- _a9_0" tabindex="0">Allow essential and optional cookies</button>