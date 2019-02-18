from selenium import webdriver

from features.pages.googleMainPage import GoogleMainPage
from features.pages.googleResultsPage import GoogleResultsPage


def before_scenario(context, scenario):
    context.location = "https://google.com"
    context.browser = webdriver.Chrome('/Users/artem/Documents/Pycharm Projects/Test/features/drivers/chromedriver')
    context.browser.get(context.location)

    context.googleMainPage = GoogleMainPage(
        context.browser, context.location)
    context.googleResultsPage = GoogleResultsPage(
        context.browser, context.location)