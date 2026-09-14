from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser=webdriver.Chrome()
sleep(2)
browser.get("https://youtube.com")
sleep(5)
elements=browser.find_elements("name","search_query")
elements.send_keys("indian foods")
sleep(2)
elements.send_keys(Keys.ENTER)
sleep(100)