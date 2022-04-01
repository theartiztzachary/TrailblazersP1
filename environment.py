from behave.runner import Context
from selenium import webdriver

from poms.log_in_home import LogInHome


def before_all(context:Context): ## need to add a driver, all poms, and set an implicit wait
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.log_in_home = LogInHome(context.driver)
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.quit()

