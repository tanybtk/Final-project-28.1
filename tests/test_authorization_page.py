# python -m pytest -v --tb=line tests/test_authorization_page.py

from pages.authorization_page import AuthorizationPage
from settings import url_test_page

class TestAuthPage():
    def testTC01_authorization_form_is_opened(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.the_authorization_form_is_open()

    def test_TC02_position_of_the_logo_and_slogan(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.position_of_the_logo_and_slogan()

    def test_TC03_position_of_the_tab_menu(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.position_of_the_tab_menu()

    def test_TC04_default_auth_type(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.default_auth_type()

    def test_TC05_auto_modification_of_authentication_type(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.auto_modification_of_authentication_type()

    def test_TC06_link_to_the_password_recovery_form(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.link_to_the_password_recovery_form()

    def test_TC07_link_to_the_registration_form(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.link_to_the_registration_form()

    def test_TC08_link_to_the_user_agreement_page(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.link_to_the_user_agreement_page()

    def test_TC09_link_fut_to_the_user_agreement_page(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.link_fut_to_the_user_agreement_page()

    def test_TC10_authorization_with_blank_fields(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.authorization_with_blank_fields()

    def test_TC11_sql_injection_in_a_text_field(self, browser):
        auth_page = AuthorizationPage(browser, url_test_page)
        auth_page.open()
        auth_page.sql_injection_in_a_text_field()