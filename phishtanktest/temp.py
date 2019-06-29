from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.request
import socket
import urllib3
import re
import requests
import csv


count =0
with open('test.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    #column = [row for row in reader] 所有列
    column = [row['url'] for row in reader] #取得只有url的列，这些url是放在列表中的
for i in column:
    driver=webdriver.PhantomJS()
    driver.get(str(i))
    time.sleep(3)
    pagesource = driver.page_source
    html_parse = BeautifulSoup(pagesource)
    temp = html_parse.findAll("script")
print(temp)
