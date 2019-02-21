from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class CentralBankWarningPage(BasePage):

    elementPath = {
        "Предупреждения": (
            By.XPATH, "//div[@id = 'content']/p"),
        "EN": (
            By.XPATH, "//a[text() = 'EN']"),
    }
