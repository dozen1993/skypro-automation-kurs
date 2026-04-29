from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
blue_button='btn-primary'
click_button=driver.find_element(By.CLASS_NAME, blue_button)
click_button.click()
sleep(5)
driver.quit()