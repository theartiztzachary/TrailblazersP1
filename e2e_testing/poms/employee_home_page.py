from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class EmployeeHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def cancel_reimbursement_button(self):
        return self.driver.find_element(By.ID, "cancel-button")

    def reimbursement_id(self):
        return self.driver.find_element(By.ID, "reimbursementID")

    def submit_button(self):
        return self.driver.find_element(By.ID, "submitButton")
