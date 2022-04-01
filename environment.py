from behave.runner import Context
from selenium import webdriver

from poms.table_test_home import TableHome

def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.table_test_home = TableHome(context.driver)
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.quit()