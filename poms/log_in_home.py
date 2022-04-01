from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LogInHome:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def employee_username_bar(self):
        return self.driver.find_element(By.ID, "employeeUsername")

    def employee_password_bar(self):
        return self.driver.find_element(By.ID, "employeePassword")

    def submit_button(self):
        return self.driver.find_element(By.ID, "searchButton")

    def get_title(self):
        return self.driver.title


