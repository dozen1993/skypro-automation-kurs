from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver =webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
driver.maximize_window()
waiter=WebDriverWait(driver, 40)
waiter.until(
    EC.presence_of_element_located((By.ID,'landscape'))
)
image_3=driver.find_element(By.ID,'award')
src_3=image_3.get_attribute('src')
print(f'SRC 3-й картинки: {src_3}')

driver.quit()