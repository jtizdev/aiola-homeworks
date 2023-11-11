from selenium.webdriver.common.by import By


class BankPageSelectors:
    # Banking Page Selectors
    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, "div.ng-scope button.btn-primary")
    CUSTOMER_DROPDOWN = (By.CSS_SELECTOR, "#userSelect option:nth-child(3)")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "div.ng-scope form button")
