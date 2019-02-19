from nose.tools import assert_equals
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

screenDir = "/Users/cberteh/Documents/Python Projects/tz_cbr/features/screenshots"
pagesDir = "/Users/artem/Documents/Pycharm Projects/Test/features/pages"


class BasePage(object):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.timeout = 30
        self.implicit_wait = 15

    def waitTillSpecificElementIsNotDisplayed(self, element):
        try:
            wait = WebDriverWait(self.browser, self.implicit_wait)
            expected_element = EC.visibility_of_element_located(element)
            wait.until(expected_element)
            return True
        except TimeoutError:
            raise

    def openUrlSite(self, url):
        self.browser.get("http://" + url)

    def setValueInField(self, field, value):
        self.browser.find_element(*self.elementPath[field]).send_keys(value)

    def clickOnElement(self, element):

        self.browser.find_element(*self.elementPath[element]).click()

    def getTextFromElement(self, element):
        try:
            a = self.browser.find_element(*self.elementPath[element])
            time.sleep(1)
        except KeyError:
            print("Element {} does not exist".format(element))
        text = a.text
        return text

    def isElementExists(self, element):
        try:
            self.browser.find_element(*self.elementPath[element])
            time.sleep(1)
            return 1
        except KeyError:
            print("Element {} does not exist".format(element))
        return 0

    def checkUrlOpenSite(self, url):
        assert_equals(self.browser.url, url)

    def makeScreenshot(self):
        self.browser.get_screenshot_as_file(screenDir)
