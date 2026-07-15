import pytest
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
from time import sleep


@pytest.fixture
def demo():
    driver=Chrome()
    driver.maximize_window()
    driver.get("https://demoapps.qspiders.com/ui?scenario=1")
    sleep(4)
    yield driver
    driver.close()
