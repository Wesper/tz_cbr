from selenium.webdriver.common.by import By

from features.pages.basePage import BasePage


class GoogleMainPage(BasePage):

    url = "https://www.google.com/"

    elementPath = {
        "Поиск": (
            By.NAME, "q"),
        "Поиск в google": (
            By.NAME, "btnK")
    }
