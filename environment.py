from behave.runner import Context
from selenium import webdriver
from poms.submit_home import SubmitHome


def before_all(context: Context):
    # we need to add a driver to the context
    context.driver = webdriver.Chrome("chromedriver.exe")
    # we need to add all poms to the context
    context.submit_home = SubmitHome(context.driver)
    # we need to set an implicit wait for the context
    context.driver.implicitly_wait(1) # this helps prevent "flakey tests"


def after_all(context: Context):
    context.driver.quit()