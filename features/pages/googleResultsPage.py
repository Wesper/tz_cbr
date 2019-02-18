from selenium.webdriver.common.by import By

from features.pages.basePage import BasePage


class GoogleResultsPage(BasePage):

    element_path = {
        "cbr.ru": (
            By.XPATH, "//link[@href='https://www.cbr.ru/']")
    }
