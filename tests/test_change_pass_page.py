# python -m pytest -v --tb=line tests/test_change_pass_page.py

import pytest
from pages.change_pass_page import ChangePassPage
from settings import url_reset_page


class TestChangePassPage():

    def test_TC12_email_field_validation_valid_data(self, browser):
        change_pass_page = ChangePassPage(browser, url_reset_page)
        change_pass_page.open()
        change_pass_page.email_field_validation_valid_data()

    def test_TC13_go_back_button(self, browser):
        change_pass_page = ChangePassPage(browser, url_reset_page)
        change_pass_page.open()
        change_pass_page.go_back_button()

    def test_TC14_link_fut_to_the_user_agreement_page(self, browser):
        change_pass_page = ChangePassPage(browser, url_reset_page)
        change_pass_page.open()
        change_pass_page.link_to_the_user_agreement_page()

    def test_TC15_default_password_recovery_type(self, browser):
        change_pass_page = ChangePassPage(browser, url_reset_page)
        change_pass_page.open()
        change_pass_page.default_password_recovery_type()

    @pytest.mark.xfail
    def test_TC16_phone_field_validation_valid_data(self, browser):
        """ Поле принимает 11-значное число в случае если первая цифра 3, 7 или 8.
        В остальных случаях поле принимает 10-значное число """
        change_pass_page = ChangePassPage(browser, url_reset_page)
        change_pass_page.open()
        change_pass_page.phone_field_validation_valid_data()


    def test_TC17_password_recovery_with_blank_fields(self, browser):
        change_pass_page = ChangePassPage(browser, url_reset_page)
        change_pass_page.open()
        change_pass_page.password_recovery_with_blank_fields()


    def test_TC18_sql_injection_in_a_text_field(self, browser):
        change_pass_page = ChangePassPage(browser, url_reset_page)
        change_pass_page.open()
        change_pass_page.sql_injection_in_a_text_field()