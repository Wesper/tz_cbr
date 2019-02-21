from features.pages.CentralBankAboutPage import CentralBankAboutPage
from features.pages.CentralBankIPPage import CentralBankIPPage
from features.pages.CentralBankMainPage import CentralBankMainPage
from features.pages.CentralBankWTPage import CentralBankWTPage
from features.pages.CentralBankWarningPage import CentralBankWarningPage
from features.pages.GoogleMainPage import GoogleMainPage
from features.pages.GoogleResultsPage import GoogleResultsPage

class NeededPage(object):

    def NeededPage(self, field):
        if self.GoogleMainPage.pageName.lower() == field.lower():
            return GoogleMainPage(self.browser, self.browser.current_url)
        elif self.GoogleResultsPage.pageName.lower() == field.lower():
            return GoogleResultsPage(self.browser, self.browser.current_url)
        elif self.CentralBankAboutPage.pageName.lower() == field.lower():
            return CentralBankAboutPage(self.browser, self.browser.current_url)
        elif self.CentralBankIPPage.pageName.lower() == field.lower():
            return CentralBankIPPage(self.browser, self.browser.current_url)
        elif self.CentralBankMainPage.pageName.lower() == field.lower():
            return CentralBankMainPage(self.browser, self.browser.current_url)
        elif self.CentralBankWarningPage.pageName.lower() == field.lower():
            return CentralBankWarningPage(self.browser, self.browser.current_url)
        elif self.CentralBankWTPage.pageName.lower() == field.lower():
            return CentralBankWTPage(self.browser, self.browser.current_url)