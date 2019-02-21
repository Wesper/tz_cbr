from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class CentralBankAboutPage(BasePage):

    elementPath = {
        "Предупреждение": (
            By.XPATH, "//a[text*()='Предупреждение']")
    }
