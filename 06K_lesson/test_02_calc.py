from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc():
    driver=webdriver.Chrome()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    driver.maximize_window()
    input_delay=driver.find_element(By.ID, 'delay')
    input_delay.click()
    input_delay.clear()
    input_delay.send_keys('45')
    keys=driver.find_element(By.CLASS_NAME,'keys')
    keys.find_element(By.XPATH,"//span[text()='7']").click()
    keys.find_element(By.XPATH,"//span[text()='+']").click()
    keys.find_element(By.XPATH,"//span[text()='8']").click()
    keys.find_element(By.XPATH,"//span[text()='=']").click()
    waiter = WebDriverWait(driver, 46)
    waiter.until( EC.text_to_be_present_in_element((By.CLASS_NAME,'screen'),'15'))
    assert  driver.find_element(By.CLASS_NAME,'screen').text == '15'
    driver.quit()