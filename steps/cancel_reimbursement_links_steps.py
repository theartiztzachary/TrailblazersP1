from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains

@when(u'I click on the cancel reimbursement link')
def step_impl(context):
    context.employee_home_page.cancel_reimbursement_page().click()


@when(u'I should be on the cancel reimbursement home page')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(title_contains("Trailblazers Reimbursement Systems - Cancel Reimbursement"))


