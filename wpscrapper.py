import time
from selenium import webdriver
from datetime import datetime
PATH = r"C:\Users\josep\Downloads\chromedriver.exe"
driver = webdriver.Chrome(PATH)
url = 'https://www.chollometro.com/categorias/electronica'
driver.get(url)

