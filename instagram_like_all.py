#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import math
from time import sleep
import sys

f = open(".credentials", "r")
USERNAME = f.readline()
PASSWORD= f.readline()

# we check number of arguments
if(len(sys.argv) < 2):
    print("You need to specify target username!")
    sys.exit()
else:
    username = sys.argv[1]

# setting up headless browser
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options) 


browser = webdriver.Firefox()
browser.set_window_position(0, 0)
browser.set_window_size(800, 500)

#graphical demonstration

browser = webdriver.Firefox()
browser.set_window_position(0, 0)
browser.set_window_size(800, 500)

# load start page
browser.get("https://www.instagram.com/accounts/login/")
sleep(0.8)

# loggin into instagram
user_name=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/div[1]/input')
password=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/div[1]/input')
user_name.send_keys(USERNAME)
password.send_keys(PASSWORD)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span[1]/button').click()

sleep(1)

# accessing target profile
browser.get("https://www.instagram.com/" + username + "/")
sleep(2)

body = browser.find_element_by_tag_name("body")
posts = browser.find_element_by_xpath('/html/body/span/section/main/article/div/div[1]')
num_posts = int(browser.find_element_by_xpath("/html/body/span/section/main/article/header/section/ul/li[1]/span/span").text)

# we click first picture
first_pic = browser.find_element_by_xpath("/html/body/span/section/main/article/div/div[1]/div[1]/div[1]")
first_pic.click()
body.send_keys(Keys.ENTER)
sleep(0.8)

# next picture button
button = browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/a")

# loop thorugh all pictures
for i in range(num_posts -1 ):
    try:
        hearth = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/article/div[2]/section[1]/a[1]")
        if(hearth.text == "Like"):
            hearth.click()
    except:
        print("err")
    button.click()
    sys.stdout.write('\r')
    
    percentage = (i / (num_posts-2) * 100)
    # the exact output you're looking for:
    x = (43 / num_posts) * i
    x = int(round (x, 0))
    sys.stdout.write("Liking(%d/%d): [%-40s] %d%%" % (i, num_posts-2, '='*x, percentage))
    sys.stdout.flush()
    
    sleep(0.5)
print()
browser.close()
