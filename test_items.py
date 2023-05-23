import time

from selenium.webdriver.common.by import By


def test_check_the_basket_button_exist(browser, language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    time.sleep(10)
    assert basket_button.is_displayed(), "The Basket button in the page"
