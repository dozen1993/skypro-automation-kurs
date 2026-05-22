from selenium import webdriver
from pages.main_page_calc import MainPageCalc


def test_calc():
    browser = webdriver.Chrome()
    main_page = MainPageCalc(browser)
    main_page.delay(45)
    main_page.number_seven()
    main_page.plus_operator()
    main_page.number_eight()
    main_page.button_equals()
    result = main_page.result()
    assert result == '15'
    main_page.close_browser()
