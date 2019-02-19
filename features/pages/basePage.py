from nose.tools import assert_equals
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

screenDir = "/Users/cberteh/Documents/Python Projects/tz_cbr/features/screenshots"
pagesDir = "/Users/cberteh/Documents/Python Projects/tz_cbr/features/pages"

class BasePage(object):
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 30
        self.implicit_wait = 15

    elementPath = {}

    def waitTillSpecificElementIsNotDisplayed(self, element):
        try:
            wait = WebDriverWait(self.browser, self.implicit_wait)
            expected_element = EC.visibility_of_element_located(element)
            wait.until(expected_element)
            return True
        except TimeoutError:
            raise

    def openUrlSite(self, url):
        a = {"gjfjf" : ("1", "2")}
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

    def findCurrentPageContext(self, element):
        for page in os.listdir(pagesDir):
            try:
                if self.page[0, len(page) - 3].elementPath[element].__class__ == 'tuple':
                    return page[0, len(page) - 3]
            except KeyError:
                pass


