from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
login='username'
passw='password'
input_login=driver.find_element(By.ID, login)
input_pass=driver.find_element(By.ID,passw)
sign_button='fa-sign-in'
click_sign_button=driver.find_element(By.CLASS_NAME, sign_button)
input_login.send_keys('tomsmith')
sleep(2)
input_pass.send_keys('SuperSecretPassword!')
sleep(2)
click_sign_button.click()
sleep(10)
driver.quit()