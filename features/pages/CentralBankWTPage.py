from selenium.webdriver.common.by import By

from features.pages.BasePageObj import BasePage


class CentralBankWTPage(BasePage):

    pageName = "Написать благодарность"

    elementPath = {
        "Ваша благодарность": (
            By.ID, "MessageBody"),
        "Я согласен": (
            By.NAME, "Agreement"),
        "Три полоски": (
            By.CLASS_NAME, "burger"),
        "О сайте": (
            By.XPATH, "//li/a[@href='/About/' and @class='pseudo']")
    }
