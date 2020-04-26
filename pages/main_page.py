from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage): #MainPage наследник класса BasePage
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_form(self):
        login_link1 = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link1.click()

    def add_good_to_basket(self):
        addBasketButton = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        addBasketButton.click()

    def check_good(self):
        bookName = self.browser.find_element(*MainPageLocators.BOOK_NAME)
        bookPrice = self.browser.find_element(*MainPageLocators.BOOK_PRICE)
        bookNameBasket = self.browser.find_element(*MainPageLocators.BOOK_NAME_IN_BASKET)
        bookPriceBasket = self.browser.find_element(*MainPageLocators.BOOK_PRICE_IN_BASKET)
        errorTextMass = "Expected: '"+ bookName.text +"' "+ bookPrice.text +". But got '"+ bookNameBasket.text +"' "+ bookPriceBasket.text
        assert (bookName.text == bookNameBasket.text) & (bookPrice.text == bookPriceBasket.text), "ERROR: " + errorTextMass