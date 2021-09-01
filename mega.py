# /usr/bin/python3
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import random
import string
from faker import Faker
fake = Faker()
import os
os.system('cls')
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Mega Account Creator - Remastered - Selenium Version/Mod - by thelinuxuser-choice")

import colorama
from colorama import Fore, Style, init

red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
blue = Fore.LIGHTBLUE_EX
yellow = Fore.YELLOW
dblue = Fore.BLUE
GREEN = Fore.GREEN
white = Fore.WHITE
colorama.init(autoreset=True)

created = 0

banner = f"""{white}

 ███▄ ▄███▓▓█████   ▄████  ▄▄▄            ███▄    █ ▒███████▒
{red}▓██▒▀█▀ ██▒▓█   ▀  ██▒ ▀█▒▒████▄          ██ ▀█   █ ▒ ▒ ▒ ▄▀░
▓██    ▓██░▒███   ▒██░▄▄▄░▒██  ▀█▄       ▓██  ▀█ ██▒░ ▒ ▄▀▒░ 
▒██    ▒██ ▒▓█  ▄ ░▓█  ██▓░██▄▄▄▄██      ▓██▒  ▐▌██▒  ▄▀▒   ░
{blue}▒██▒   ░██▒░▒████▒░▒▓███▀▒ ▓█   ▓██▒ ██▓ ▒██░   ▓██░▒███████▒
░ ▒░   ░  ░░░ ▒░ ░ ░▒   ▒  ▒▒   ▓▒█░ ▒▓▒ ░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒
░  ░      ░ ░ ░  ░  ░   ░   ▒   ▒▒ ░ ░▒  ░ ░░   ░ ▒░░░▒ ▒ ░ ▒
░      ░      ░   ░ ░   ░   ░   ▒    ░      ░   ░ ░ ░ ░ ░ ░ ░
       ░      ░  ░      ░       ░  ░  ░           ░   ░ ░  {cyan}  Account Creator 
                                      ░             ░       {yellow}  Remastered
                                                              {magenta} Selenium Version/Mod
            {GREEN}> Github - thelinuxuser-choice <                                             
"""
print(banner)
input("[ENTER] Click Enter to Start And Make sure to read README.txt >")
with open("emails.txt", "r") as fd:
            try:
              for line in fd:
                 #print("\n\n\n[Ready] Debug: STARTING")
                 #time.sleep(3)
                 path = "driver\chromedriver.exe"
                 driver = webdriver.Chrome(path)
                 time.sleep(3)
                 os.system('cls')
                 print(banner)
                 email = line.split("\n")
                 domain = "@xitroo.de"
                 surname = fake.name()
                 lastname = fake.name()
                 characters = string.ascii_letters + string.digits + string.punctuation
                 password = ''.join(random.choice(characters) for i in range(8))
                 print(f"{cyan}[Starting] Debug: START")
                 print(f"{yellow}[Email] Email: " + email[0] + domain)
                 print(f"{yellow}[Password] Password: " + password)
                 print(f"{cyan}[Mega] Debug: Open Mega.nz")
                 driver.get("https://mega.nz/register")
                 time.sleep(17)
                 print(f"{GREEN}[Mega] Debug: Cookie")
                 driver.find_element_by_xpath("//*[@id='bodyel']/section[1]/div[4]/div[1]/div[2]/button[1]").click()
                 time.sleep(2)
                 print(f"{GREEN}[Mega] Debug: Firstname")
                 driver.find_element_by_xpath("//*[@id='register-firstname-registerpage2']").click()
                 time.sleep(0.5)
                 driver.find_element_by_xpath("//*[@id='register-firstname-registerpage2']").send_keys(surname)
                 time.sleep(2)
                 print(f"{GREEN}[Mega] Debug: Lastname")
                 driver.find_element_by_xpath("//*[@id='register-lastname-registerpage2']").click()
                 time.sleep(0.5)
                 driver.find_element_by_xpath("//*[@id='register-lastname-registerpage2']").send_keys(lastname)
                 time.sleep(2)
                 print(f"{GREEN}[Mega] Debug: Email")
                 driver.find_element_by_xpath("//*[@id='register-email-registerpage2']").click()
                 time.sleep(0.5)
                 driver.find_element_by_xpath("//*[@id='register-email-registerpage2']").send_keys(email[0] + domain)
                 time.sleep(2)
                 print(f"{GREEN}[Mega] Debug: Password")
                 driver.find_element_by_xpath("//*[@id='register-password-registerpage2']").click()
                 time.sleep(0.5)
                 driver.find_element_by_xpath("//*[@id='register-password-registerpage2']").send_keys(password)
                 time.sleep(2)
                 print(f"{GREEN}[Mega] Debug: Verify Password")
                 driver.find_element_by_xpath("//*[@id='register-password-registerpage3']").click()
                 time.sleep(0.5)
                 driver.find_element_by_xpath("//*[@id='register-password-registerpage3']").send_keys(password)
                 time.sleep(2)
                 print(f"{magenta}[Mega] Debug: Checkbox 1")
                 driver.find_element_by_xpath("//*[@id='register_form']/div[8]/label").click()
                 time.sleep(2)
                 print(f"{magenta}[Mega] Debug: Checkbox 2")
                 driver.find_element_by_id("register-check-registerpage2").click()
                 time.sleep(2)
                 print(f"{magenta}[Mega] Debug: Click Button")
                 driver.find_element_by_xpath("//*[@id='register_form']/button").click()
                 time.sleep(10)
                 print(f"{cyan}[Xitroo] Debug: Open Xitroo")
                 driver.get("https://xitroo.de/#" + email[0])
                 time.sleep(5)
                 print(f"{red}>> Waiting for Mail")
                 time.sleep(3)
                 print(f"{red}[Xitroo] Debug: Click Email in Inbox")
                 try:
                     print(f"{red}>> Trying Desktop Element")
                     driver.find_element_by_xpath("//*[@id='mailList']/tr").click()
                     pass 
                 except NoSuchElementException:
                     print(f"{red}>> Trying Mobile Element")
                     driver.find_element_by_xpath("//*[@id='mailListMobile']").click()
                     pass 
                 except :
                     print(f"{red}[Warning] Email Confirmation not recieved!")
                     pass 
                 time.sleep(2)
                 iframe = driver.find_element_by_id("mailContentFrame")
                 time.sleep(1)
                 print(f"{cyan}[Xitroo] Debug: Switch to Iframe")
                 driver.switch_to.frame(iframe)
                 time.sleep(2)
                 print(f"{blue}[Xitroo] Debug: Click Verification Button")
                 driver.find_element_by_xpath("//*[@id='frameContent']/table/tbody/tr[1]/td[2]/table/"
                                         "tbody/tr/td/table/tbody/tr/td").click()
                 time.sleep(3)
                 print(f"{blue}[Xitroo] Debug: Switch to Parent Iframe")
                 driver.switch_to.parent_frame()
                 time.sleep(1)
                 print(f"{cyan}[Chrome tab] Debug: Switch to Second Tab")
                 driver.switch_to.window(driver.window_handles[1])
                 time.sleep(3)
                 print(f"{blue}[Mega] Debug: Password")
                 driver.find_element_by_id("login-password2").click()
                 time.sleep(0.5)
                 driver.find_element_by_id("login-password2").send_keys(password)
                 time.sleep(2)
                 print(f"{blue}[Mega] Debug: Click Button")
                 driver.find_element_by_xpath("//*[@id='login_form']/button").click()
                 time.sleep(5)
                 with open("Accounts.txt", "a+") as f:
                     f.write(f"{email[0]}{domain}:{password}\n")
                     created +=1
                     ctypes.windll.kernel32.SetConsoleTitleW(f"Mega Account Creator - Created accounts : {created}  - Remastered - Selenium Version/Mod - by thelinuxuser-choice")
                 print(f"\n{cyan}[Mega Account Creator] Debug: Done")
                 driver.quit()
            except NoSuchElementException:  
                os.system('cls')
                print(f"{yellow}[Error] An error occured while Creating a Account Reasons are [Names you have entered in emails.txt is taken] ")
                time.sleep(2)
                print
                pass 
                
input("[EXIT] Press Enter to Exit >")                
# If you saw the source and learned from this please add a star on this github repo 
# Much more coming soon , stay tuned !
