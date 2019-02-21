from selenium.webdriver.common.by import By

from features.pages.BasePageObj import BasePage


class CentralBankAboutPage(BasePage):

    pageName = "О сайте"

    elementPath = {
        "Предупреждение": (
            By.XPATH, "//a[text*()='Предупреждение']")
    }
