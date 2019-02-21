from selenium.webdriver.common.by import By

from features.pages.BasePageObj import BasePage


class GoogleResultsPage(BasePage):

    pageName = "результатов поиска"

    elementPath = {
        "cbr.ru": (
            By.XPATH, "//link[@href='https://www.cbr.ru/']")
    }
