######################################################################
# Auto Send SBD to BitTrex v1
# by Murat Tatar
# January 2018
######################################################################

######################################################################
# --!-- WARNING! --!--
# YOU MUST, FIRST TRY WITH yesreal=0
# WHILE SETUP OR CONFIGURATION
# YOU MAY LOSE SBD/STEEM
# !! ALL RESPONSIBILITIES YOUR OWN !!
######################################################################

# import needed moduls
import os
import requests
import re
import time
from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
import win32api, win32con
from controls import *
import pyperclip

######################################################################
# --!-- WARNING! --!--
# YOU MUST, FIRST TRY WITH yesreal = 0
# WHILE SETUP OR CONFIGURATION
# YOU MAY LOSE SBD/STEEM
# !! ALL RESPONSIBILITIES YOUR OWN !!
######################################################################

yesreal = 0
######################################################################


# steemit user name and private key
user = 'murattatar'
prv_key = 'P5TaJB1wk1BuXbeN1mKeY1mDEG1LjmN9xfzA75y8uvB8ekMV6vX6'


# for SBD wallet
toexchange = 'bittrex'
memo = '71d09fa0ea954f3a9d2'

######################################################################

def e():
  exit()


## Auto Send SBD to BitTrex  #########################################


# First, Login into Steemit

page = web.Chrome("chromedriver.exe")
url = 'https://steemit.com/login.html'
page.get(url)
page.implicitly_wait(30)
page.set_window_position(0,0)
page.set_window_size(1360, 768)


userbox = page.find_element_by_name('username')
userbox.send_keys(user) # user 'murattatar'
time.sleep(.2)
keybox = page.find_element_by_name('password')
keybox.send_keys(prv_key)
time.sleep(.2)
butonSL = page.find_element_by_xpath(".//button[@type='submit']")
time.sleep(.2)
keybox.send_keys(Keys.RETURN)
time.sleep(2)


url = 'https://steemit.com/@'+user+'/transfers'
page.get(url)
time.sleep(2)
page.implicitly_wait(30)

# find element created via javasctipt that there is not in ctrl+u
js_code = '''
b = document.getElementsByTagName('button');
return b
'''

redembutton = page.execute_script(js_code)
print redembutton

for btn in redembutton:
  element_text = btn.text
  if element_text == 'BUY STEEM OR STEEM POWER':
    # Redeem Rewards (Transfer To Balance)
    # BUY STEEM OR STEEM POWER
    #btn.click()

    # You Sould div[5] to div[4]
    sbdbutton = page.find_element_by_xpath('.//div[@class="UserWallet"]/div[5]/div/span')
    sbdbutton.click()

    transferbutton = page.find_element_by_link_text('Transfer')
    transferbutton.click()
    time.sleep(1)

    # fill "to"
    Cliq(900,405)
    pyperclip.copy(toexchange)
    PressHoldRelease('ctrl', 'v')
    Cliq(715,225)

    # fill "amount"
    time.sleep(1)
    # send ALL SBD to > someone or exchange
    if yesreal ==1:      
      Cliq(515,500)
    else:
      # send 0.001 SBD to > someone or exchange
      Cliq(503,463); Write('0.001')


    # fill "memo"
    time.sleep(1)
    Cliq(515,584)
    time.sleep(1)
    pyperclip.copy(memo)
    PressHoldRelease('ctrl', 'v')

    time.sleep(1)
    Press('enter')

    time.sleep(1)
    Cliq(650,380)
    pyperclip.copy(prv_key)
    PressHoldRelease('ctrl', 'v')
    Press('enter')


    e()

