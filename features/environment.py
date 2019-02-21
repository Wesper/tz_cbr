from selenium import webdriver

from features.pages.BasePageObj import BasePage
from features.pages.CentralBankAboutPage import CentralBankAboutPage
from features.pages.CentralBankIPPage import CentralBankIPPage
from features.pages.CentralBankMainPage import CentralBankMainPage
from features.pages.CentralBankWTPage import CentralBankWTPage
from features.pages.CentralBankWarningPage import CentralBankWarningPage
from features.pages.GoogleMainPage import GoogleMainPage
from features.pages.GoogleResultsPage import GoogleResultsPage


def before_scenario(context, scenario):
    context.location = "https://yandex.ru"
    context.browser = webdriver.Chrome('/Users/artem/Documents/Pycharm Projects/Test/features/drivers/chromedriver')
    context.browser.get(context.location)

    context.GoogleMainPage = GoogleMainPage(
        context.browser, context.location)
    context.GoogleResultsPage = GoogleResultsPage(
        context.browser, context.location)
    context.BasePage = BasePage(
        context.browser, context.location)
    context.CentralBankAboutPage = CentralBankAboutPage(
        context.browser, context.location)
    context.CentralBankIPPage = CentralBankIPPage(
        context.browser, context.location)
    context.CentralBankMainPage = CentralBankMainPage(
        context.browser, context.location)
    context.CentralBankWarningPage = CentralBankWarningPage(
        context.browser, context.location)
    context.CentralBankWTPage = CentralBankWTPage(
        context.browser, context.location)