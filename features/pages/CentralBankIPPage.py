from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class CentralBankIPPage(BasePage):

    elementPath = {
        "Написать благодарность": (
            By.XPATH, "//h2[text()='Написать благодарность']")
    }
