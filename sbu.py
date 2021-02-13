from bs4 import BeautifulSoup
import pandas as pd
#import sys
#!{sys.executable} -m pip install selenium

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

#firefox_binary = FirefoxBinary('/usr/bin/firefox/')
#driver = webdriver.Firefox(firefox_binary=firefox_binary)

#driver.get("https://tableau.stonybrook.edu/vizql/t/Public/w/Covid-19Accessible/v/WeeklyCases/viewData/sessions/1FCBAC071FD84953A29E128E587A10A2-1:2/views/14068672024067378307_6414820709505016832?maxrows=200&viz=%7B%22worksheet%22%3A%22SBU")

#html = driver.page_source
#soup = BeautifulSoup(html)

driver = webdriver.Firefox()
driver.get("https://tableau.stonybrook.edu/vizql/t/Public/w/Covid-19Accessible/v/WeeklyCases/viewData/sessions/1FCBAC071FD84953A29E128E587A10A2-1:2/views/14068672024067378307_6414820709505016832?maxrows=200&viz=%7B%22worksheet%22%3A%22SBU")

html = driver.page_source
soup = BeautifulSoup(html)

print(soup.find("table"))