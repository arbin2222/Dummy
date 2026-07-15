import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)

@pytest.fixture
def demo():
    driver = Chrome(
        service=Service(ChromeDriverManager().install()),
        options=o
    )
    driver.maximize_window()
    driver.get("https://demoapps.qspiders.com/ui?scenario=1")
    sleep(4)
    yield driver
    driver.close()