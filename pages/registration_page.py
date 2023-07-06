from .basic_page import BasicPage
from .locators import BaseLocators, RegPageLocators, EmailConfirmPageLocators, UserAgreementPageLocators


class RegistrationPage(BasicPage):
    # TC19 проверка расположения полей ввода, кнопки "Зарегистрироваться", ссылки на пользовательское соглашение
    def location_of_input_fields_and_buttons_and_links(self):
        assert self.is_element_present(RegPageLocators.REG_FIRST_NAME_INPUT_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_REGISTER_BUTTON_PAGE_RIGHT), "element not found"
        assert self.is_element_present(RegPageLocators.REG_USER_AGREEMENT_LINK_PAGE_RIGHT), "element not found"

    # TC20 проверка ввода валидных данных
    def text_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_FIRST_NAME_INPUT), "element found"

    # TC21 проверка ввода валидных данных в поле ввода (тел., мейл)
    def email_or_phone_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT_VALUE)
        value = element.get_attribute("value")
        assert input_text == value, "email or phone do not match"
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element found"

    # TC22 проверка ввода валидного пароля
    def password_field_validation_valid_data(self, input_text):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_not_element_present(RegPageLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element found"

    # TC23 проверка регистрации с валидными данными
    def registration_with_valid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegPageLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_element_present(EmailConfirmPageLocators.EMAIL_CONF_HEADING), "element not found"

    # TC24 проверка ссылки под кнопкой "Зарегистрироваться" на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(RegPageLocators.REG_USER_AGREEMENT_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # TC25 проверка ссылки в футере на страницу с пользовательским соглашением
    def link_fut_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(RegPageLocators.REG_PRIVACY_POLICY_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # TC26 проверока ввода невалидных данных в  текстовом поле
    def text_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_FIRST_NAME_INPUT), "element not found"

    # TC27 проверка ввода невалидного email или мобильного телефона
    def email_or_phone_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_INVALID_EMAIL_OR_PHONE_INPUT), "element not found"

    # TC28 проверка ввода невалидных данных пароля
    def password_field_validation_invalid_data(self, input_text):
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(input_text)
        self.find_element(BaseLocators.BODY).click()
        assert self.is_element_present(RegPageLocators.REG_ERROR_INVALID_PASSWORD_INPUT), "element not found"

    # TC29 проверка регистрации с невалидными данными
    def registration_with_invalid_data(self, first_name, last_name, email_phone, password):
        self.find_element(RegPageLocators.REG_FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(RegPageLocators.REG_LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(RegPageLocators.REG_EMAIL_PHONE_INPUT).send_keys(email_phone)
        self.find_element(RegPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.find_element(RegPageLocators.REG_ENTER_BUTTON).click()
        assert self.is_not_element_present(EmailConfirmPageLocators.EMAIL_CONF_HEADING), "element found"