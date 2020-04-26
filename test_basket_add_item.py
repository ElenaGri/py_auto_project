from .pages.main_page import MainPage


def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page.add_good_to_basket()
    page.solve_quiz_and_get_code()
    page.chack_good()