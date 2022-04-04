from behave import when, then, given
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains


@given(u'I am on the Log In home page')
def step_impl(context):
    context.driver.get("file:///C:/Users/pompa/Desktop/HTML_Stuff/for-fetchP1.html")


@when(u'I enter {employeeUsername} into the input bar')
def step_impl(context, employeeUsername: str):
    context.log_in_home.employee_username_bar().send_keys(employeeUsername)


@when(u'I type out {employeePassword} into my input bar')
def step_impl(context, employeePassword: str):
    context.log_in_home.employee_password_bar().send_keys(employeePassword)


@when(u'I click the Submit button')
def step_impl(context):
    context.log_in_home.submit_button().click()


@then(u'I should be on a page with the title Home Screen')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(title_contains("WELCOME"))
    assert context.driver.title == "WELCOME"
