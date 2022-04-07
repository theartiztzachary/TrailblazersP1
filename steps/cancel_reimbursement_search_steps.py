import time

from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains, alert_is_present


@given(u'I am on the cancel reimbursement home page')
def step_impl(context):
    context.driver.get("C:/Users/Tashawn/Desktop/TrailblazersP1/cancel_reimbursement_home_page.html")


@when(u'I enter {reimbursement_id} into the text box')
def step_impl(context, reimbursement_id: int):
    context.employee_home_page.reimbursement_id().send_keys(reimbursement_id)


@when(u'I click the submit button')
def step_impl(context):
    context.employee_home_page.submit_cancel_reimbursement_button().click()