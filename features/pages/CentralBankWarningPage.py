from selenium.webdriver.common.by import By

from features.pages.BasePageObj import BasePage


class CentralBankWarningPage(BasePage):

    pageName = "Предупреждения"

    elementPath = {
        "Предупреждения": (
            By.XPATH, "//div[@id = 'content']/p"),
        "EN": (
            By.XPATH, "//a[text() = 'EN']"),
    }
