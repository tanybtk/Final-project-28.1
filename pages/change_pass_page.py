from settings import valid_phone, valid_email, sql_injection
from .basic_page import BasicPage
from .locators import AuthPageLocators, ChangePassPageLocators, UserAgreementPageLocators, \
    RejectedRequestPageLocators, BaseLocators


class ChangePassPage(BasicPage):

    # TC12 проверка  поля ввода  валидного email
    def email_field_validation_valid_data(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_MAIL).click()
        username_input = self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT)
        email = valid_email()
        username_input.send_keys(email)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT_VALUE)
        value = element.get_attribute("value")
        assert email == value, "email do not match"

    # TC13 проверка кнопки на форму авторизации
    def go_back_button(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_GO_BACK_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in self.browser.current_url, \
            "url do not match"

    #TC14 проверка ссылки в футере на страницу с пользовательским соглашением
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(ChangePassPageLocators.CHANGE_PASS_PRIVACY_POLICY_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

        # TC15 проверка восстановления пароля по умолчанию
    def default_password_recovery_type(self):
        assert self.is_element_present(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "element not found"

        # TC16 проверка поля ввода валидного номера телефона

    def phone_field_validation_valid_data(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_PHONE).click()
        phone = valid_phone()
        self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT).send_keys(phone)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT_VALUE)
        value = element.get_attribute("value")
        assert ("7" + str(phone)) == value, "phone do not match"

    # TC17 проверка восстановления пароля с незаполненными полями
    def password_recovery_with_blank_fields(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_PHONE).click()
        self.find_element(ChangePassPageLocators.CHANGE_PASS_CONTINUE_BUTTON).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassPageLocators.CHANGE_PASS_ERROR_ENTER_PHONE_NUMBER), \
            "element not found"


    # TC18 проверка текстового поля на SQL-инъекции
    def sql_injection_in_a_text_field(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT).send_keys(sql_injection())
        self.find_element(ChangePassPageLocators.CHANGE_PASS_CONTINUE_BUTTON).click()
        assert self.is_element_present(RejectedRequestPageLocators.REJECTED_REQUEST_HEADING), "element not found"
        assert self.is_element_present(RejectedRequestPageLocators.REJECTED_REQUEST_INFO), "element not found"