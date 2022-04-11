import unittest
import aos_methods as methods
import aos_locators as locators

class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user(): # test_ in the name is mandatory

        methods.setUp()
        methods.validate_home_page_texts_links()
        methods.validate_top_navigation_menu()
        methods.validate_contact_us_form()
        methods.validate_social_media_link()
        methods.create_new_user()
        methods.validate_new_user_display()
        methods.log_out()
        methods.login(locators.new_username, locators.new_password)
        methods.validate_new_user_display()
        methods.checkout_shopping_cart()
        methods.log_out()
        methods.login(locators.new_username, locators.new_password)
        methods.validate_order_page()
        methods.delete_order()
        methods.log_out()
        methods.teardown()

