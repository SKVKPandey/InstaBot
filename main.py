ChromeDriverPath = "WebDriver\chromedriver.exe"

from seleniumwire import webdriver as wd1
from selenium import webdriver as wd2
from time import sleep

def start(proxy_status, message):

    proxiesfile = open("proxies.txt", "r")
    proxies = list(set([x[:-1] for x in proxiesfile.readlines()]))

    with open('usernames.txt', 'r') as usersfile:

        user_count = 0

        users_list = [x.split(':') for x in usersfile.readlines()]
        proxy = proxies[user_count%len(proxies)].split(':')

        for user in users_list:

            name_val = user[0]
            key_val = ''
            if '\n' in user[1]:
                key_val = user[1][:-1]
            else:
                key_val = user[1]

            with open('accounts.txt') as accountsfile:

                accounts_list = [x for x in accountsfile.readlines()]

                try:

                    if proxy_status=='Y':

                        proxy_string = f"http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"

                        options = {
                        'proxy': {
                            'http': proxy_string,
                            'https': proxy_string,
                            'no_proxy': 'localhost,127.0.0.1'
                            }
                        }

                        chrome_options = wd1.ChromeOptions()
                        chrome_options.add_argument('--headless')
                        chrome_options.add_argument('--no-sandbox')
                        chrome_options.add_argument('--ignore-certificate-errors-spki-list')
                        chrome_options.add_argument('--ignore-ssl-errors')
                        chrome = wd1.Chrome('WebDriver\chromedriver.exe', options=chrome_options, seleniumwire_options=options)

                        chrome.get("https://www.instagram.com/")

                        sleep(3)

                        submit = chrome.find_element("xpath", "//button[@tabindex='0']").click()

                    else:
                        chrome_options = wd2.ChromeOptions()
                        chrome_options.add_argument('--headless')
                        chrome_options.add_argument('--no-sandbox')
                        chrome_options.add_argument('--ignore-certificate-errors-spki-list')
                        chrome_options.add_argument('--ignore-ssl-errors')
                        chrome = wd1.Chrome('WebDriver\chromedriver.exe', options=chrome_options, seleniumwire_options=options)
                        chrome = wd2.Chrome(ChromeDriverPath)
                        chrome.get("https://www.instagram.com/")

                    sleep(8)                        

                    username = chrome.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
                    password = chrome.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')

                    username.send_keys(f'''{name_val}''')
                    password.send_keys(f'''{key_val}''')
                    sleep(1)

                    submit = chrome.find_element("xpath", "//button[@type='submit']").click()
                    sleep(10)       

                    for account in accounts_list:

                        try:
                            if '\n' in account[0]:
                                chrome.get(f"https://www.instagram.com/{account[:-1]}")
                                sleep(5)
                            else:
                                chrome.get(f"https://www.instagram.com/{account}")
                                sleep(5)

                            submit = chrome.find_element("xpath", "//button[@type='button']").click()

                            sleep(10)

                            dm = chrome.find_element("xpath", "//button[@tabindex='0']")
                            dm.send_keys(f'''{message}\n''')

                            print(f"\n{name_val} sent message to {account}")

                        except Exception as e:
                            chrome.close()
                            print(f"\nError: {e}")
                            start()

                except Exception as e:
                    chrome.close()
                    print(f"\nError: {e}")

            user_count+=1
            chrome.close()
            exit()


proxy_status = input("\nUse Proxies(Y/n): ")
message = input("\nEnter Message: ")

start(proxy_status, message)
