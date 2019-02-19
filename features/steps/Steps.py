from behave import *
from nose.tools import assert_false

from features.pages.centralBankAboutPage import CentralBankAboutPage
from features.pages.centralBankIPPage import CentralBankIPPage
from features.pages.centralBankMainPage import CentralBankMainPage
from features.pages.centralBankWTPage import CentralBankWTPage
from features.pages.centralBankWarningPage import CentralBankWarningPage
from features.pages.googleMainPage import GoogleMainPage
from features.pages.googleResultsPage import GoogleResultsPage

use_step_matcher("re")
saved_text =""

def contextPage(context, field):
    if str(context.googleMainPage.elementPath).find(field) != -1:
        return GoogleMainPage(context, url="")
    elif str(context.googleResultsPage.elementPath).find(field) != -1:
        return GoogleResultsPage(context)
    elif str(context.centralBankAboutPage.elementPath).find(field) != -1:
        return CentralBankAboutPage(context)
    elif str(context.centralBankIPPage.elementPath).find(field) != -1:
        return CentralBankIPPage(context)
    elif str(context.centralBankMainPage.elementPath).find(field) != -1:
        return CentralBankMainPage(context)
    elif str(context.centralBankWarningPage.elementPath).find(field) != -1:
        return CentralBankWarningPage(context)
    elif str(context.centralBankWTPage.elementPath).find(field) != -1:
        return CentralBankWTPage(context)

@given('Зашли на сайт "([^"]*)"')
def step_impl(context, url):
    context.basePage.openUrlSite(url)


@step('Нашли ссылку "([^"]*)"')
@step('Проверили, что появилось поле "([^"]*)"')
def step_impl(context, field):
    page = contextPage(context, field)
    page.isElementExists(field)


@step('В поле "([^"]*)" ввели значение "([^"]*)"')
@step('Ввели в поле "([^"]*)" значение "([^"]*)"')
def step_impl(context, field, value):
    context.basePage.setValueInField(field, value)


@step('Сменили язык страницы на "([^"]*)"')
@step('Нажали на раздел "([^"]*)"')
@step('Поставили галочку "([^"]*)"')
@step('Открыли раздел "([^"]*)"')
@step('Нажали на ссылку "([^"]*)"')
@step('Нажали на кнопку "([^"]*)"')
def step_impl(context, element):
    context.basePage.clickOnElement(element)


@step("Проверили, что открыт нужный сайт")
def step_impl(context):
    context.basePage.checUrlOpenSite(context.centralBankMainPage.url)


@step("Сделали скриншот")
def step_impl(context):
    context.basePage.makeScreenshot()


@step('Запомнили текст "([^"]*)"')
def step_impl(context, element):
    saved_text = context.basePage.getTextFromElement(element)
    return saved_text


@step("Проверили, что текст отличается от запомненного текста ранее")
def step_impl(context):
    assert_false(saved_text, context.basePage.getTextFromElement())