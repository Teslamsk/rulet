from selenium.webdriver.common.by import By


class MainPageLocators:
    WHEEL = (By.CSS_SELECTOR, ".wheel")
    COUNTER = (By.CSS_SELECTOR, ".text-2xl")
    RESULT = (By.CSS_SELECTOR, ".hidden .flex .flex .flex .previous-rolls-item:nth-child(10) .inline-block")
