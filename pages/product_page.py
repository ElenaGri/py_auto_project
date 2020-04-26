from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): #MainPage наследник класса BasePage

    def add_good_to_basket(self):
        addBasketButton = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        addBasketButton.click()

    def check_good(self):
        bookName = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        bookPrice = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        bookNameBasket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET)
        bookPriceBasket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET)
        errorTextMass = "Expected: '" + bookName.text + "' " + bookPrice.text + ". But got '" + bookNameBasket.text + "' " + bookPriceBasket.text
        assert (bookName.text == bookNameBasket.text) & (bookPrice.text == bookPriceBasket.text), "ERROR: " + errorTextMass

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"