#!/usr/bin/env python3

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os, sys

phoneNumber = '' # Here the phone number to connect.
ex_name = '' # Change the name.

driver = webdriver.Firefox() # Change to use Chrome.
driver.get('https://bumble.com/get-started')

sleep(1)

input('Please hit <Return> after accepting cookies')

sleep(1)

phoneBtn = driver.find_element(By.XPATH, "//span[text()='Use cell phone number']")
phoneBtn.click()

sleep(0.5)

phoneInput = driver.find_element(By.ID, 'phone')
phoneInput.send_keys(phoneNumber)

sleep(0.5)

phoneAction = driver.find_element(By.XPATH, "//span[text()='Continue']")
phoneAction.click()

input('Please hit <Return> when the code received by message is entered (and the Captcha).')

sleep(2)

os.system('clear')

driver.find_element(By.XPATH, "//div[@class='p-3']")

print('Connected!')

sleep(3)

os.system('clear')

def like():
    likeBtn = driver.find_element(By.XPATH, "//span[@data-qa-icon-name='floating-action-yes']")
    sleep(0.5)
    likeBtn.click()

def dislike():
    dislikeBtn = driver.find_element(By.XPATH, "//span[@data-qa-icon-name='floating-action-no']")
    sleep(0.5)
    dislikeBtn.click()

while True:
    if ex_name != '':
        like()
    elif ex_name in driver.page_source:
        dislike()
    else:
        like()
