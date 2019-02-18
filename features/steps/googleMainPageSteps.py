from behave import *

from nose.tools import assert_equals, assert_true

use_step_matcher("re")

@Given('Open site google.com')
def openStartPage(context):
    assert_equals(context.browser.current_url, "{}".format(
        context.googleMainPage.url))
    print("1")
    pass

@Step('Make sure that the "([^"]*)" field is displayed')
def checkFieldOnGoogleMainPage(context, field):
    context.googleMainPage.wait_till_specific_element_is_not_displayed(
        context.googleMainPage.element_path[field])
    print("2")
    pass

@Step('Entered in the "([^"]*)" field the value "([^"]*)"')
def enterValueInFieldOnGoogleMainPage(context, field, value):
    context.googleMainPage.set_value_in_field(field, value)
    print("3")
    pass

@Step('Clicked on the "([^"]*)" button')
def clickElementOnGoogleMainPage(context, element):
    context.googleMainPage.click_on_element(element)
    print("4")
    pass