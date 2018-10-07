#!/usr/bin/python3
from selenium import webdriver
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import math
import os
from time import sleep
import sys

#This script is a bit more dirty. Downloads all images of a profile.
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options) 

f = open(".credentials", "r")
USERNAME = f.readline()
PASSWORD= f.readline()

followers = []
with open('/root/data/followers', encoding="utf-8") as f:
    lines = f.readlines()
i = 0
for line in lines:
    if(i % 4 == 0) and (line != ''):
        followers.append(line.strip("\n"))
    i+=1

browser.get("https://www.instagram.com/accounts/login/")
sleep(2)

# loggin into instagram
user_name=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/div[1]/input')
password=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/div[1]/input')
user_name.send_keys(USERNAME)
password.send_keys(PASSWORD)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span[1]/button').click()

sleep(1)
for username in followers:
    print(username)

    directory = "/root/data/instaBackup/" + username 
    if not os.path.exists(directory):
        os.makedirs(directory)

        
        # accessing target profile
    browser.get("https://www.instagram.com/" + username + "/")
    sleep(1)

    try:
        body = browser.find_element_by_tag_name("body")
        posts = browser.find_element_by_xpath('/html/body/span/section/main/article/div/div[1]')
        num_posts = int(browser.find_element_by_xpath("/html/body/span/section/main/article/header/section/ul/li[1]/span/span").text)
        if(num_posts >=1):

            # we click first picture
            first_pic = browser.find_element_by_xpath("/html/body/span/section/main/article/div/div[1]/div[1]/div[1]")
            first_pic.click()
            body.send_keys(Keys.ENTER)
            sleep(3)

            # next picture button
            button = browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/a")


            for i in range(num_posts ):
                try:
                    image= browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/article/div[1]/div/div/div[1]/img")
                    link = image.get_attribute("src")
                    command = "wget -qc -P "+ directory+" "+link
                    os.system(command)
                    sleep(0.3)
                    
                except Exception as e: 
                    y =e
                if(i < num_posts-1):
                    button.click()
                sys.stdout.write('\r')
                
                percentage = (i / (num_posts-1) * 100)
                # the exact output you're looking for:
                x = (43 / num_posts) * i
                x = int(round (x, 0))
                sys.stdout.write("Saving(%d/%d): [%-40s] %d%%" % (i, num_posts-1, '='*x, percentage))
                sys.stdout.flush()
                
                sleep(1)
            print()
    except Exception as e:
        print(e)
print()
browser.close()
