from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class HelperFunc(object):
    """ set a timeout limit """
    __TIMEOUT = 5

    """ create the constructor and use super() for smooth inheritance """

    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        """ driver wait inclued the timeout time"""
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def maximize(self):
        self._driver.maximize_window()

    def close(self):
        self._driver.quit()

    def get_title(self):
        self._driver.title()

    def accept_tcs(self):
        self._driver.switch_toframe('sc-hKMtZM eukFrW').alert().accept()

    def clear(self):
        self._driver.clear()

    def action(self):
        ActionChains(self._driver)


    """ Helper functions to find locators """

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_css(self, css):
        return self._driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

    def find_by_class(self, class_name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
