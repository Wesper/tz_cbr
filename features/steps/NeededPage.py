from features.pages.CentralBankAboutPage import CentralBankAboutPage
from features.pages.CentralBankIPPage import CentralBankIPPage
from features.pages.CentralBankMainPage import CentralBankMainPage
from features.pages.CentralBankWTPage import CentralBankWTPage
from features.pages.CentralBankWarningPage import CentralBankWarningPage
from features.pages.GoogleMainPage import GoogleMainPage
from features.pages.GoogleResultsPage import GoogleResultsPage


def sdsdsd(context, field):
    if str(context.googleMainPage.elementPath).find(field) != -1:
        return GoogleMainPage(context.browser, context.browser.current_url)
    elif str(context.googleResultsPage.elementPath).find(field) != -1:
        return GoogleResultsPage(context.browser, context.browser.current_url)
    elif str(context.centralBankAboutPage.elementPath).find(field) != -1:
        return CentralBankAboutPage(context.browser, context.browser.current_url)
    elif str(context.centralBankIPPage.elementPath).find(field) != -1:
        return CentralBankIPPage(context.browser, context.browser.current_url)
    elif str(context.centralBankMainPage.elementPath).find(field) != -1:
        return CentralBankMainPage(context.browser, context.browser.current_url)
    elif str(context.centralBankWarningPage.elementPath).find(field) != -1:
        return CentralBankWarningPage(context.browser, context.browser.current_url)
    elif str(context.centralBankWTPage.elementPath).find(field) != -1:
        return CentralBankWTPage(context.browser, context.browser.current_url)



def neededPage(context, field):
    if str(context.GoogleMainPage.elementPath).find(field) != -1:
        return GoogleMainPage(context.browser, context.browser.current_url)
    elif str(context.GoogleResultsPage.elementPath).find(field) != -1:
        return GoogleResultsPage(context.browser, context.browser.current_url)
    elif str(context.CentralBankAboutPage.elementPath).find(field) != -1:
        return CentralBankAboutPage(context.browser, context.browser.current_url)
    elif str(context.CentralBankIPPage.elementPath).find(field) != -1:
        return CentralBankIPPage(context.browser, context.browser.current_url)
    elif str(context.CentralBankMainPage.elementPath).find(field) != -1:
        return CentralBankMainPage(context.browser, context.browser.current_url)
    elif str(context.CentralBankWarningPage.elementPath).find(field) != -1:
        return CentralBankWarningPage(context.browser, context.browser.current_url)
    elif str(context.CentralBankWTPage.elementPath).find(field) != -1:
        return CentralBankWTPage(context.browser, context.browser.current_url)