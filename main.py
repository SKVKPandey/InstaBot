ChromeDriverPath = "WebDriver\chromedriver.exe"

import sys
from seleniumwire import webdriver
from time import sleep
from pyautogui import press, write
from user_agent import generate_user_agent
from tkinter import *

def start(proxy_status, message):

    proxiesfile = open("proxies.txt", "r")
    proxies = [x[:-1] for x in proxiesfile.readlines()]

    with open('usernames.txt', 'r') as usersfile:

        user_count = 0

        users_list = [x.split(',') for x in usersfile.readlines()]
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

                        chrome_options = webdriver.ChromeOptions()
                        chrome_options.add_argument('--proxy-server=%s' % proxy[0]+':'+proxy[1])

                        chrome = webdriver.Chrome(ChromeDriverPath, chrome_options=chrome_options)
                        chrome.get("https://www.instagram.com/")

                        sleep(5)

                        write(proxy[2])
                        press('tab')
                        write(proxy[3])
                        press('enter')

                        sleep(30)

                        for _ in range(6):
                            press('tab')
                        press('enter')

                    else:
                        chrome = webdriver.Chrome(ChromeDriverPath)
                        chrome.get("https://www.instagram.com/")

                    sleep(5)                        

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

                            write(f"{message}")
                            press('enter')
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

proxy_status = input("Use Proxies(Y/n): ")
message = input("Enter Message: ")

start(proxy_status, message)