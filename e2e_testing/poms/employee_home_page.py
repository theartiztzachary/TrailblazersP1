from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class EmployeeHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def cancel_reimbursement_page(self):
        return self.driver.find_element(By.ID, "cancelButton")

    def reimbursement_id(self):
        return self.driver.find_element(By.ID, "reimbursement_id")

    def submit_cancel_reimbursement_button(self):
        return self.driver.find_element(By.ID, "submitButton")

    def get_alert(self):
        return self.driver.switch_to.alert
