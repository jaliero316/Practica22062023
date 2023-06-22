import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Telegram_bot import TelegramBot
from mongodb import MongoDB
chrome_driver = webdriver.Chrome()

bot = TelegramBot()
db = MongoDB()

chrome_driver.get("https://www.wikipedia.org/")
print(chrome_driver.title)
