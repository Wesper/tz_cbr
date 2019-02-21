from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class CentralBankWTPage(BasePage):

    elementPath = {
        "Ваша благодарность": (
            By.ID, "MessageBody"),
        "Я согласен": (
            By.NAME, "Agreement"),
        "Три полоски": (
            By.CLASS_NAME, "burger"),
        "О сайте": (
            By.XPATH, "//a[@href='/About/']")
    }
