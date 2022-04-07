from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class TableHome:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_bar(self):
        element: WebElement = self.driver.find_element(By.ID, "number-input")
        return element

    def history_button(self):
        element: WebElement = self.driver.find_element(By.ID, "history-button")
        return element

    def pending_button(self):
        element: WebElement = self.driver.find_element(By.ID, "pending-button")
        return element

    def approved_button(self):
        element: WebElement = self.driver.find_element(By.ID, "approved-button")
        return element

    def first_reimbursement_id(self):
        element: WebElement = self.driver.find_element(By.ID, "0")
        return element

    def pending_total(self):
        element: WebElement = self.driver.find_element(By.ID, "pending-total")
        return element

    def approved_total(self):
        element: WebElement = self.driver.find_element(By.ID, "approved-total")
        return element