import pytest
import time
from selenium import webdriver
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    time.sleep(5)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()