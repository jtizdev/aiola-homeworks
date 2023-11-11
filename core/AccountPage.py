from BankingPageSelectors.AccountPage import AccountSelectors


class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.selectors = AccountSelectors()

    def deposit_money(self, amount):
        self.driver.find_element(*self.selectors.DEPOSIT_BUTTON).click()
        self.driver.find_element(*self.selectors.DEPOSIT_INPUT).send_keys(amount)
        self.driver.find_element(*self.selectors.DEPOSIT_CONFIRM_BUTTON).click()

    def withdraw_money(self, amount):
        self.driver.find_element(*self.selectors.WITHDRAWAL_BUTTON).click()
        self.driver.find_element(*self.selectors.WITHDRAWAL_INPUT).send_keys(amount)
        self.driver.find_element(*self.selectors.WITHDRAWAL_CONFIRM_BUTTON).click()

    def view_transactions(self):
        self.driver.find_element(*self.selectors.TRANSACTIONS_BUTTON).click()
