from behave import *
from nose.tools import assert_false

from features.steps.NeededPage import neededPage

use_step_matcher("re")
saved_text =""


@given('Зашли на сайт "([^"]*)"')
def step_impl(context, arg):
    neededPage(context, arg).openUrlSite(arg)


@step('Нашли ссылку "([^"]*)"')
@step('Проверили, что появилось поле "([^"]*)"')
def step_impl(context, arg):
    neededPage(context, arg).isElementExists(arg)


@step('В поле "([^"]*)" ввели значение "([^"]*)"')
@step('Ввели в поле "([^"]*)" значение "([^"]*)"')
def step_impl(context, arg1, arg2):
    neededPage(context, arg1).setValueInField(arg1, arg2)


@step('Сменили язык страницы на "([^"]*)"')
@step('Нажали на раздел "([^"]*)"')
@step('Поставили галочку "([^"]*)"')
@step('Открыли раздел "([^"]*)"')
@step('Нажали на ссылку "([^"]*)"')
@step('Нажали на кнопку "([^"]*)"')
def step_impl(context, arg):
    neededPage(context, arg).clickOnElement(arg)


@step("Проверили, что открыт нужный сайт")
def step_impl(context):
    context.basePage.checUrlOpenSite(context.centralBankMainPage.url)


@step("Сделали скриншот")
def step_impl(context):
    context.basePage.makeScreenshot()


@step('Запомнили текст "([^"]*)"')
def step_impl(context, arg):
    saved_text = neededPage(context, arg).getTextFromElement(arg)
    return saved_text


@step("Проверили, что текст отличается от запомненного текста ранее")
def step_impl(context):
    assert_false(saved_text, context.basePage.getTextFromElement())