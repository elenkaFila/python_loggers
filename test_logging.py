import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    request.addfinalizer(driver.quit)
    return driver


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        driver.save_screenshot(f'screenshots/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S_exception.png")}')
        print(exception)


def test_logging(driver):
    driver.get('https://habr.com/ru/companies/selectel/articles/861436/')
    find_button = driver.find_element('xpath', "//a[@data-test-id='search-button']")
    find_button.click()
    time.sleep(2)
    find_field = driver.find_element('xpath', "//input[contains(@class,'tm-search__input')]")
    find_field.send_keys('привет')
    find_field.send_keys(Keys.ENTER)
    driver.save_screenshot(f'screenshots/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S_finish_test.png")}')
