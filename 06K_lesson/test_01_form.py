from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    driver=webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    field_first_name=driver.find_element(By.CSS_SELECTOR,"[name='first-name']")
    field_first_name.click()
    field_first_name.send_keys('Иван')
    field_last_name=driver.find_element(By.CSS_SELECTOR,"[name='last-name']")
    field_last_name.click()
    field_last_name.send_keys('Петров')
    field_address=driver.find_element(By.CSS_SELECTOR,"[name='address']")
    field_address.click()
    field_address.send_keys('Ленина,55-3')
    field_city=driver.find_element(By.CSS_SELECTOR,"[name='city']")
    field_city.click()
    field_city.send_keys('Москва')
    field_country=driver.find_element(By.CSS_SELECTOR,"[name='country']")
    field_country.click()
    field_country.send_keys('Россия')
    field_email=driver.find_element(By.CSS_SELECTOR,"[name='e-mail']")
    field_email.click()
    field_email.send_keys('test@skypro.com')
    field_phone=driver.find_element(By.CSS_SELECTOR,"[name='phone']")
    field_phone.click()
    field_phone.send_keys('+7985899998787')
    field_job=driver.find_element(By.CSS_SELECTOR,"[name='job-position']")
    field_job.click()
    field_job.send_keys('QA')
    field_company=driver.find_element(By.CSS_SELECTOR,"[name='company']")
    field_company.click()
    field_company.send_keys('SkyPro')
    button_submit=driver.find_element(By.CLASS_NAME,'btn-outline-primary')
    driver.execute_script('arguments[0].click();', button_submit)
    waiter = WebDriverWait(driver, 10)
    waiter.until(
        EC.presence_of_element_located((By.ID,'zip-code')))
    assert'alert-danger'in driver.find_element(By.ID,'zip-code').get_attribute('class')
    fields=['first-name', 'last-name','address','city','country','e-mail','phone', 'job-position','company']
    for field_id in fields:
        field_class= driver.find_element(By.ID,field_id).get_attribute('class')
        assert 'alert-success' in field_class
    driver.quit()