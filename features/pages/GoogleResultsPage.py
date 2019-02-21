from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class GoogleResultsPage(BasePage):

    elementPath = {
        "cbr.ru": (
            By.XPATH, "//link[@href='https://www.cbr.ru/']")
    }
