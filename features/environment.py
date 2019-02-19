from selenium import webdriver

from features.pages.basePage import BasePage
from features.pages.centralBankAboutPage import CentralBankAboutPage
from features.pages.centralBankIPPage import CentralBankIPPage
from features.pages.centralBankMainPage import CentralBankMainPage
from features.pages.centralBankWTPage import CentralBankWTPage
from features.pages.centralBankWarningPage import CentralBankWarningPage
from features.pages.googleMainPage import GoogleMainPage
from features.pages.googleResultsPage import GoogleResultsPage


def before_scenario(context, scenario):
    context.location = "https://yandex.ru"
    context.browser = webdriver.Chrome('/Users/artem/Documents/Pycharm Projects/Test/features/drivers/chromedriver')
    context.browser.get(context.location)

    context.googleMainPage = GoogleMainPage(
        context.browser, context.location)
    context.googleResultsPage = GoogleResultsPage(
        context.browser, context.location)
    context.basePage = BasePage(
        context.browser, context.location)
    context.centralBankAboutPage = CentralBankAboutPage(
        context.browser, context.location)
    context.centralBankIPPage = CentralBankIPPage(
        context.browser, context.location)
    context.centralBankMainPage = CentralBankMainPage(
        context.browser, context.location)
    context.centralBankWarningPage = CentralBankWarningPage(
        context.browser, context.location)
    context.centralBankWTPage = CentralBankWTPage(
        context.browser, context.location)