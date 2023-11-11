from BankingPageSelectors.BankPage import BankPageSelectors


class BankPage:
    def __init__(self, driver):
        self.driver = driver
        self.selectors = BankPageSelectors()

    def click_customer_login_button(self):
        self.driver.find_element(*self.selectors.CUSTOMER_LOGIN_BUTTON).click()

    def click_on_name_list(self):
        self.driver.find_element(*self.selectors.CUSTOMER_DROPDOWN).click()

    def click_login_button(self):
        self.driver.find_element(*self.selectors.LOGIN_BUTTON).click()
