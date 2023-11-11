from selenium.webdriver.common.by import By


class TransactionPageSelectors:
    # Banking Page Selectors
    TRANSACTIONS_PAGE_TABLE = (By.CSS_SELECTOR, "body div.ng-scope table.table tbody")
    BACK_BUTTON = (By.CSS_SELECTOR, "body div.ng-scope div.fixedTopBox button:nth-child(1)")
    TRANSACTIONS_ROW = (By.CSS_SELECTOR, "#anchor0")
