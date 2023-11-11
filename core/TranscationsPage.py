from BankingPageSelectors.TranscationsPage import TransactionPageSelectors


class TransactionPage:
    def __init__(self, driver):
        self.driver = driver
        self.selectors = TransactionPageSelectors()

    def transactions_page_is_empty(self):
        return self.driver.find_element(
            *TransactionPageSelectors.TRANSACTIONS_PAGE_TABLE).is_not_displayed()

    def click_back_button(self):
        self.driver.find_element(*TransactionPageSelectors.BACK_BUTTON).click()

    def transactions_page_is_not_empty(self):
        return self.driver.find_element(
            *TransactionPageSelectors.TRANSACTIONS_ROW).is_displayed()
