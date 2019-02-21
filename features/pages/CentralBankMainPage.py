from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class CentralBankMainPage(BasePage):
    url = "http://cbr.ru/"

    elementPath = {
        "Интернет-приемная": (
            By.XPATH, "//a[@href='/Reception/']")
    }
