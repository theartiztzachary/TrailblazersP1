from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains


@given(u'I am on the Submit Reimbursement page')
def step_impl(context):
    context.driver.get("file:///C:/Users/master/Desktop/Html_stuff/Day3%20Javascript/for_submitP1.html")


@when(u'I enter {employeeId} in the EmployeeId textbox')
def step_impl(context, employeeId: int):
    context.submit_home.submit_employee_id().send_keys(employeeId)


@when(u'I enter {amount} in the Amount textbox')
def step_impl(context, amount: int):
    context.submit_home.submit_amount().send_keys(amount)


@when(u'I enter {reason}  in the Reason textbox')
def step_impl(context, reason: str):
    context.submit_home.submit_reason().send_keys(reason)


@when(u'I enter {reimbursementComment} in the Reimbursement Comment textbox')
def step_impl(context, reimbursementComment: str):
    context.submit_home.submit_reimbursement_comment().send_keys(reimbursementComment)


@when(u'I click Submit button')
def step_impl(context):
    context.submit_home.submit_button().click()


@then(u'I should be on the Reimbursement home page')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(title_contains("Reimbursement Home"))
    assert context.driver.title == "Reimbursement Home"

