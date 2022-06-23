from selenium import webdriver
from helpers.helper_fundamental import HelperFunc


def get_browser(browser):
    if browser == "firefox":
        return HelperFunc(webdriver.Firefox())
    elif browser == "chrome":
        return HelperFunc(webdriver.Chrome())
    else:
        HelperFunc(webdriver.Firefox())
