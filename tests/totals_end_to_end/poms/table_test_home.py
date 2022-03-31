from selenium.webdriver.opera.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class TableHome:
    def __init__(self, driver: WebDriver):
        self.driver = driver