from behave import when, then, given
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains


@given(u'I am on the Log In home page')
def step_impl(context):
    context.driver.get("file:///D:/PythonProjects/TrailblazersP1/front_end_files/landing-page.html")

@when(u'I enter {employeeUsername} into the input bar')
def step_impl(context, employeeUsername: str):
    context.log_in_home.employee_username_bar().send_keys(employeeUsername)

@when(u'I type out {employeePassword} into my input bar')
def step_impl(context, employeePassword: str):
    context.log_in_home.employee_password_bar().send_keys(employeePassword)

@when(u'I click the login button')
def step_impl(context):
    context.log_in_home.submit_button().click()

@then(u'I should be on the employee home page')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(title_contains("Trailblazers Reimbursement Systems - Home"))
    assert context.driver.title == "Trailblazers Reimbursement Systems - Home"
