from behave.runner import Context
from selenium import webdriver

from tests.totals_end_to_end.poms.table_test_home import TableHome

def before_all(context: Context):
    context.driver = webdriver.Opera("tests/totals_end_to_end/operadriver.exe")
    context.table_test_home = TableHome(context.driver)
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.quit()