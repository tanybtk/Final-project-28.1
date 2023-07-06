import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome for test..")
    chrome_link = webdriver.Chrome()
    chrome_link.maximize_window()
    yield chrome_link
    print("\nquit ")
    chrome_link.quit()
