from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/inputs")
input_field='[type="number"]'
click_input_field=driver.find_element(By.CSS_SELECTOR, input_field)
click_input_field.send_keys("12345")
sleep(5)
click_input_field.clear()
click_input_field.send_keys("54321")
sleep(5)
driver.quit()