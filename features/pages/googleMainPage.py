from selenium.webdriver.common.by import By

from features.pages.basePage import BasePage


class GoogleMainPage(BasePage):
    url = "https://www.google.com/"

    element_path = {
        "поиск": (
            By.NAME, "q"),
        "поиск в google": (
            By.NAME, "btnK")
    }
