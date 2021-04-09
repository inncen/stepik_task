from selenium.common.exceptions import NoSuchElementException


class TestPage:
    def test_page_contains_add_to_basket_button(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        button = None
        try:
            button = browser.find_element_by_class_name('btn-add-to-basket')
        except NoSuchElementException:
            ...
        finally:
            assert button is not None, \
                f"Page not contains add to basket button"
