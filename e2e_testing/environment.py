from behave.runner import Context
from selenium import webdriver

from e2e_testing.poms.employee_home_page import EmployeeHomePage


# this module allows for interactions with elements on web page

def before_all(context: Context):
    context.driver = webdriver.Chrome("e2e_testing/chromedriver.exe")
    context.employee_home_page = EmployeeHomePage(context.driver)  # this is the POM
    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
