#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep, gmtime, strftime
import os
import sys

# Script is designed to run on a certain period and like first picture of a target profile

f = open(".credentials", "r")
USERNAME = f.readline()
PASSWORD= f.readline()

TARGETS = ["tilenkocjan"]

def like_pic(username):
    browser.get("https://www.instagram.com/" + username + "/")
    sleep(1)

    body = browser.find_element_by_tag_name("body")
    try:
        first_pic = browser.find_element_by_xpath("/html/body/span/section/main/article/div/div[1]/div[1]/div[1]")
        first_pic.click()
        body.send_keys(Keys.ENTER)
        sleep(1)

        hearth = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/article/div[2]/section[1]/a[1]")
        if(hearth.text == "Like"):
            hearth.click()
            out = "echo " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": "
            print("*")
            out += 'user {}: new picture liked'.format(username) + ">> /root/data/instaStalk.log"
            os.system(out)
    except:
        print("err")

# setting up a browser
# setting up headless browser
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options) 

# load start page
browser.get("https://www.instagram.com/accounts/login/")
sleep(1)

# loggin into instagram
user_name=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/div[1]/input')
password=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/div[1]/input')
user_name.send_keys(USERNAME)
password.send_keys(PASSWORD)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span[1]/button').click()
sleep(1)

for i in range(2):
    for target in TARGETS:
        like_pic(target)

browser.close()
