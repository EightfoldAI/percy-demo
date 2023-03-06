from selenium.webdriver.common.by import By

class CareerPageLocators(object):
    JOBS = (By.CSS_SELECTOR, 'a[class*="Nav_Padding"][href*="aexp"]')
    SKIP = (By.CSS_SELECTOR, 'div.wizard-footer button')
