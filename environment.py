from behave.runner import Context
from selenium import webdriver

from poms.table_test_home import TableHome
from poms.log_in_home import LogInHome

def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.table_test_home = TableHome(context.driver)
    context.log_in_home = LogInHome(context.driver)
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.quit()
