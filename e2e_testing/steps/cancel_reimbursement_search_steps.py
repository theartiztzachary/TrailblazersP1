from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains, alert_is_present


@given(u'I am on the cancel reimbursement home page')
def step_impl(context):
    # context.driver.get("C:/Users/Tashawn/Desktop/TrailblazersP1/cancel_reimbursement_home_page.html")
    context.driver.get("D:/PythonProjects/TrailblazersP1/cancel_reimbursement_home_page.html")


@when(u'I enter {reimbursement_id} into the text box')
def step_impl(context, reimbursement_id: int):
    context.employee_home_page.reimbursement_id().send_keys(reimbursement_id)


@when(u'I click the submit button')
def step_impl(context):
    context.employee_home_page.submit_cancel_reimbursement_button().click()


@then(u'I should be on a page with the title {title}')
def step_impl(context, title: str):
    # WebDriverWait(context.driver, 1).until(title_contains("Trailblazers Reimbursement Systems"))
    WebDriverWait(context.driver, 3).until(title_contains("Trailblazers Reimbursement Systems"))
    assert context.driver.title == title

@when(u'I see the alert')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(alert_is_present())
    context.employee_home_page.get_alert()

@when(u'I accept the alert')
def step_impl(context):
    context.employee_home_page.get_alert().accept()
