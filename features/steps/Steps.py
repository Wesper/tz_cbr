from behave import *
from nose.tools import assert_not_equal

from features.steps.NeededPage import NeededPage

use_step_matcher("re")
saved_text = None
page = None

@given('Зашли на сайт "([^"]*)"')
def step_impl(context, arg):
    context.BasePage.openUrlSite(arg)


@step('Нашли ссылку "([^"]*)"')
@step('Проверили, что появилось поле "([^"]*)"')
def step_impl(context, arg):
    page.isElementExists(arg)


@step('В поле "([^"]*)" ввели значение "([^"]*)"')
@step('Ввели в поле "([^"]*)" значение "([^"]*)"')
def step_impl(context, arg1, arg2):
    page.setValueInField(arg1, arg2)


@step('Сменили язык страницы на "([^"]*)"')
@step('Нажали на раздел "([^"]*)"')
@step('Поставили галочку "([^"]*)"')
@step('(?:Открыли|Выбрали) раздел "([^"]*)"')
@step('Нажали на ссылку "([^"]*)"')
@step('Нажали на кнопку "([^"]*)"')
def step_impl(context, arg):
    page.clickOnElement(arg)


@step('Проверили, что открыт нужный сайт')
def step_impl(context):
    context.BasePage.checkUrlOpenSite(page.url)


@step('Сделали скриншот')
def step_impl(context):
    context.BasePage.makeScreenshot()


@step('Запомнили текст "([^"]*)"')
def step_impl(context, arg):
    global saved_text
    saved_text = page.getTextFromElement(arg)


@step('Проверили, что текст "([^"]*)" отличается от запомненного текста ранее')
def step_impl(context, arg):
    assert_not_equal(saved_text, page.getTextFromElement(arg))

@step('(?:Открывается|Открылась)? (.*) страница')
@step('(?:Открывается|Открылась) страница? (.*)')
@step('Пользователь находится на странице? (.*)')
def step_impl(context, arg):
    global page
    page = NeededPage.NeededPage(context, arg)


@step("Отправили письмо и удалили скриншоты")
def step_impl(context):
    context.BasePage.sendEmailAndDeleteScreenshons()