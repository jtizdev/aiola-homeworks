from selenium.webdriver.common.by import By


class AccountSelectors:
    # Banking Page Selectors
    TRANSACTIONS_BUTTON = (
        By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)")
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)")
    WITHDRAWAL_BUTTON = (
        By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)")
    DEPOSIT_INPUT = (By.CSS_SELECTOR,
                     "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input")
    DEPOSIT_CONFIRM_BUTTON = (By.CSS_SELECTOR,
                             "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button")
    WITHDRAWAL_INPUT = (By.CSS_SELECTOR,
                        "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input")
    WITHDRAWAL_CONFIRM_BUTTON = (By.CSS_SELECTOR,
                                "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button")
