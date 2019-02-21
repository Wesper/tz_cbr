from selenium.webdriver.common.by import By

from features.pages.BasePageObj import BasePage


class CentralBankIPPage(BasePage):

    pageName = "Интернет-приемная"

    elementPath = {
        "Написать благодарность": (
            By.XPATH, "//h2[text()='Написать благодарность']")
    }
