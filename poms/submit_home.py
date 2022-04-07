from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class SubmitHome:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def start_submit(self):
        element: WebElement = self.driver.find_element(By.ID, "submit-button")
        return element

    def submit_employee_id(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeId")
        return element

    def submit_amount(self):
        element: WebElement = self.driver.find_element(By.ID, "amount")
        return element

    def submit_reason(self):
        element: WebElement = self.driver.find_element(By.ID, "reason")
        return element

    def submit_reimbursement_comment(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementComment")
        return element

    def submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitReimbursement")
        return element

    def get_alert(self):
        return self.driver.switch_to.alert


