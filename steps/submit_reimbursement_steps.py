from behave import when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains

@when(u'I click the Submit Reimbursement button')
def step_impl(context):
    context.submit_home.start_submit().click()

@when(u'I should be on a page with the title Home Screen')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(title_contains("Trailblazers Reimbursement Systems - Submit Reimbursement"))
    assert context.driver.title == "Trailblazers Reimbursement Systems - Submit Reimbursement"

@when(u'I enter {amount} in the Amount textbox')
def step_impl(context, amount: int):
    context.submit_home.submit_amount().send_keys(amount)

@when(u'I enter {reason}  in the Reason textbox')
def step_impl(context, reason: str):
    context.submit_home.submit_reason().send_keys(reason)

@when(u'I enter {reimbursementComment} in the Reimbursement Comment textbox')
def step_impl(context, reimbursementComment: str):
    context.submit_home.submit_reimbursement_comment().send_keys(reimbursementComment)

@then(u'I click Submit button')
def step_impl(context):
    context.submit_home.submit_button().click()


