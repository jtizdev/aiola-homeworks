import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BankingPageSelectors.AccountPage import AccountSelectors
from BankingPageSelectors.BankPage import BankPageSelectors
from BankingPageSelectors.TranscationsPage import TransactionPageSelectors
from core import AccountPage, BankPage, TranscationsPage

from BankingPageSelectors import AccountPage, BankPage, TranscationsPage


class Tests:
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  # Set implicit wait to 5 seconds
        self.url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        self.account_page_selectors = AccountPage.AccountSelectors()
        self.banking_page_selectors = BankPage.BankPageSelectors()
        self.transactions_page_selectors = TranscationsPage.TransactionPageSelectors()
        yield
        self.driver.quit()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @pytest.mark.sanity
    def test_sanity(self, setup):
        self.driver.get(self.url)

        # Explicitly wait for the customer login button to be clickable, not the best option for test
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.banking_page_selectors.CUSTOMER_LOGIN_BUTTON)).click()

        self.driver.find_element(*self.banking_page_selectors.CUSTOMER_DROPDOWN).click()
        self.driver.find_element(*BankPageSelectors.LOGIN_BUTTON).click()
        self.driver.find_element(*AccountSelectors.TRANSACTIONS_BUTTON).click()
        self.driver.find_element(*TransactionPageSelectors.BACK_BUTTON).click()
        self.driver.find_element(*AccountSelectors.DEPOSIT_BUTTON).click()
        self.driver.find_element(*AccountSelectors.DEPOSIT_INPUT).send_keys("200")
        self.driver.find_element(*AccountSelectors.DEPOSIT_CONFIRM_BUTTON).click()
        time.sleep(
            5)  # not liking to use it since it's stuck for 5 seconds, but the site server is slow so that why the test
        # was failing before, if you want to see the logic working you can debug and remove it
        self.driver.find_element(*AccountSelectors.WITHDRAWAL_BUTTON).click()
        self.driver.find_element(*AccountSelectors.WITHDRAWAL_INPUT).send_keys("100")
        self.driver.find_element(*AccountSelectors.WITHDRAWAL_CONFIRM_BUTTON).click()
        time.sleep(
            5)  # not liking to use it since it's stuck for 5 seconds, but the site server is slow so that why the test
        # was failing before, if you want to see the logic working you can debug and remove it
        self.driver.find_element(*AccountSelectors.TRANSACTIONS_BUTTON).click()
        assert self.wait_for_element(
            TransactionPageSelectors.TRANSACTIONS_ROW).is_displayed(), "Transactions page is empty"
