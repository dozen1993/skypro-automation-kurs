from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')

input_field=driver.find_element(By.CLASS_NAME, 'form-control')
input_field.click()
input_field.send_keys('SkyPro')
blue_button=driver.find_element(By.CLASS_NAME,'btn-primary')
blue_button.click()
print(blue_button.text)
driver.quit()