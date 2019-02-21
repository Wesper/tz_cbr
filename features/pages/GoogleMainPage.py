from selenium.webdriver.common.by import By

from features.pages.BasePageObj import BasePage


class GoogleMainPage(BasePage):

    pageName = "поиска"

    base_url = ""
    url = "https://www.google.com/"

    elementPath = {
        "Поиск": (
            By.NAME, "q"),
        "Поиск в google": (
            By.NAME, "btnK")
    }
