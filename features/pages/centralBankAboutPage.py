from selenium.webdriver.common.by import By

from features.pages.basePage import BasePage


class CentralBankAboutPage(BasePage):

    elementPath = {
        "Предупреждение": (
            By.XPATH, "//a[text*()='Предупреждение']")
    }
