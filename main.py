ChromeDriverPath = "WebDriver\chromedriver.exe"

from selenium import webdriver
from time import sleep
from pyautogui import press, write
from tkinter import *

def start():

    proxiesfile = open("proxies.txt", "r")
    proxies = [x[:-1] for x in proxiesfile.readlines()]
    dm = msg.get(1.0, "end-1c")

    with open('usernames.txt', 'r') as usersfile:

        count = 0

        users_list = [x.split(',') for x in usersfile.readlines()]
        proxy = proxies[count%len(proxies)].split(':')

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

                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument('--proxy-server=%s' % proxy[0]+':'+proxy[1])

                    chrome = webdriver.Chrome(ChromeDriverPath, chrome_options=chrome_options)
                    chrome.get("https://www.instagram.com/")

                    sleep(5)

                    write(proxy[2])
                    press('tab')
                    write(proxy[3])
                    press('enter')

                    sleep(25)

                    for _ in range(6):
                        press('tab')
                    press('enter')

                    sleep(3)

                    username = chrome.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
                    password = chrome.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')

                    username.send_keys(f'''{name_val}''')
                    password.send_keys(f'''{key_val}''')
                    sleep(1)

                    submit = chrome.find_element("xpath", "//button[@type='submit']").click()
                    sleep(10)       

                    for account in accounts_list:

                        if '\n' in account[0]:
                            chrome.get(f"https://www.instagram.com/{account[:-1]}")
                            sleep(4)
                        else:
                            chrome.get(f"https://www.instagram.com/{account}")
                            sleep(4)

                        for _ in range(2):
                            press('tab')
                        press('enter')      
                        sleep(2)    

                        for _ in range(2):
                            press('tab')
                        press('enter')
                        sleep(2)

                        write(f"{dm}")
                        press('enter')

                        console_data = console.get(1.0, "end-1c")
                        console.delete(1.0,END)
                        console.insert(1.0,f'{console_data}\n{name_val} sent message to {account}')

                except Exception as e:
                    chrome.close()
                    console_data = console.get(1.0, "end-1c")
                    console.delete(1.0,END)
                    console.insert(1.0,f'{console_data}\nError: {name_val} not sent message to {account}')

            count+=1

app = Tk()
app.geometry('700x700')
app.title('InstaBot')
console_label = Label(app, text = "Console").place(x = 100, y = 50)
console = Text(app, height = 15, width = 50)
console.place(x=100, y=75)
msg_label = Label(app, text = "Message").place(x = 100, y = 425)
msg = Text(app, height = 5, width = 50)
msg.place(x=100, y=450)
button = Button(app, text='Start', width=20, command = start)
button.place(x=260, y=600)
app.mainloop()