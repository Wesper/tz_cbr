import os
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from nose.tools import assert_equals
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import smtplib

screenDir = "/Users/cberteh/Documents/Python Projects/tz_cbr/features/screenshots/"
screenName = 1
addr_from = ""
password = ""
addr_to = ""


class BasePage(object):
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 30
        self.implicit_wait = 15

    pageName = "Базовая страница"

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
        time.sleep(1)
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
        assert_equals(self.browser.current_url, url)

    def makeScreenshot(self):
        global screenDir
        global screenName
        self.browser.get_screenshot_as_file(screenDir + str(screenName) + ".png")
        screenName += 1

    def sendEmailAndDeleteScreenshons(self):
        global screenName
        screenNameLocal = screenName
        msg = MIMEMultipart()
        msg['From'] = addr_from
        msg['TO'] = addr_to
        msg['Subject'] = 'Test screenshots'

        body = "Test screenshots attachments"
        msg.attach(MIMEText(body, 'plain'))

        while screenNameLocal > 1:
            screenNameLocal -= 1
            file = open(screenDir + str(screenNameLocal) + ".png", "rb")
            attach = MIMEImage(file.read())
            attach.add_header('Content-Disposition', 'attachment; filename="%s"' % screenNameLocal)
            file.close()
            msg.attach(attach)
            os.remove(screenDir + str(screenNameLocal) + ".png")

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(addr_from, password)
        server.send_message(msg)
        server.quit()
