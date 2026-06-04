from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get('http://uitestingplayground.com/ajax')
driver.implicitly_wait(16)
driver.find_element(By.CSS_SELECTOR,'#ajaxButton').click()
element = driver.find_element(By.CLASS_NAME,"bg-success")
print(element.text)
driver.quit()