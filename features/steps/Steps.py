from behave import *
from nose.tools import assert_false

use_step_matcher("re")
saved_text =""


@given('Зашли на сайт "([^"]*)"')
def step_impl(context, url):
    context.basePage.openUrlSite(url)


@step('Нашли ссылку "([^"]*)"')
@step('Проверили, что появилось поле "([^"]*)"')
def step_impl(context, field):
    context.basePage.isElementExists(field)


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