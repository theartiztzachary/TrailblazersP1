from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains


@given(u'I am on the employee home page')
def step_impl(context):
    context.driver.get("file:///C:/Users/Tashawn/Desktop/TrailblazersP1/employee_home_page.html")


@when(u'I click on the cancel reimbursement link')
def step_impl(context):
    context.employee_home_page.cancel_reimbursement_page().click()


@then(u'I should be on the cancel reimbursement home page')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(title_contains("Cancel Reimbursement"))
    context.employee_home_page.submit_cancel_reimbursement_button().click()



