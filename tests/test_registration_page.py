# python -m pytest -v --tb=line tests/test_registration_page.py

import pytest
from pages.registration_page import RegistrationPage
from settings import url_test_page, invalid_name, valid_email_or_phone, valid_password, valid_first_name, \
    valid_last_name, invalid_email_or_phone, invalid_password, valid_password2, random_int, first_name_en, \
    chinese_chars, russian_chars


class TestRegistrationPage:
    def test_TC19_location_of_input_fields_and_buttons_and_links(self, browser):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.location_of_input_fields_and_buttons_and_links()

    @pytest.mark.parametrize('input_text', valid_first_name)
    def test_TC20_text_field_validation_valid_data(self, browser, input_text):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.text_field_validation_valid_data(input_text)

    @pytest.mark.parametrize('input_text', valid_email_or_phone)
    def test_TC21_email_or_phone_field_validation_valid_data(self, browser, input_text):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.email_or_phone_field_validation_valid_data(input_text)

    @pytest.mark.parametrize('input_text', valid_password)
    def test_TC22_password_field_validation_valid_data(self, browser, input_text):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.password_field_validation_valid_data(input_text)

    @pytest.mark.parametrize('first_name', valid_first_name)
    @pytest.mark.parametrize('last_name', valid_last_name)
    @pytest.mark.parametrize('email_phone', valid_email_or_phone)
    @pytest.mark.parametrize('password', valid_password)
    def test_TC23_registration_with_valid_data(self, browser, first_name, last_name, email_phone, password):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.registration_with_valid_data(first_name, last_name, email_phone, password)

    def test_TC24_link_to_the_user_agreement_page(self, browser):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.link_to_the_user_agreement_page()

    def test_TC25_link_fut_to_the_user_agreement_page(self, browser):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.link_fut_to_the_user_agreement_page()

    @pytest.mark.parametrize('input_text', invalid_name)
    def test_TC26_text_field_validation_invalid_data(self, browser, input_text):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.text_field_validation_invalid_data(input_text)

    @pytest.mark.parametrize('input_text', invalid_email_or_phone)
    def test_TC27_email_or_phone_field_validation_invalid_data(self, browser, input_text):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.email_or_phone_field_validation_invalid_data(input_text)

    @pytest.mark.parametrize('input_text', invalid_password)
    def test_TC28_password_field_validation_invalid_data(self, browser, input_text):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.password_field_validation_invalid_data(input_text)


    @pytest.mark.parametrize('first_name', [random_int()])
    @pytest.mark.parametrize('last_name', [first_name_en()])
    @pytest.mark.parametrize('email_phone', [chinese_chars()])
    @pytest.mark.parametrize('password', [russian_chars()])
    def test_TC29_registration_with_invalid_data(self, browser, first_name, last_name, email_phone, password):
        reg_page = RegistrationPage(browser, url_test_page)
        reg_page.open_reg_page()
        reg_page.registration_with_invalid_data(first_name, last_name, email_phone, password)