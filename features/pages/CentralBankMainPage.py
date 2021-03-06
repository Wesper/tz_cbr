from selenium.webdriver.common.by import By

from features.pages.BasePageObj import BasePage


class CentralBankMainPage(BasePage):

    url = "https://www.cbr.ru/"

    pageName = "Главная"

    elementPath = {
        "Интернет-приемная": (
            By.XPATH, "//a[@href='/Reception/']")
    }
