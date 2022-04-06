from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.common.by import By


@given(u'I am on the reimbursement home page')
def step_impl(context):
    context.driver.get("file:///D:/PythonProjects/TrailblazersP1/reimb_front_end/reimbursement-history-test.html")

@when(u'I enter {employee_id} into the employee id bar')
def step_impl(context, employee_id: int):
    context.table_test_home.input_bar().send_keys(employee_id)

@when(u'I click the Get History button')
def step_impl(context):
    context.table_test_home.history_button().click()

@then(u'I can see the first entry ID is {reimbursement_id}')
def step_impl(context, reimbursement_id: int):
    wait = WebDriverWait(context.driver, 1).until(text_to_be_present_in_element((By.ID, "0"), reimbursement_id))
    assert context.table_test_home.first_reimbursement_id().text == reimbursement_id

@when(u'I click the Get Pending Sum button')
def step_impl(context):
    context.table_test_home.pending_button().click()

@then(u'I can see my pending reimbursement total is {total}')
def step_impl(context, total: float):
    wait = WebDriverWait(context.driver, 1).until(text_to_be_present_in_element((By.ID, "pending-total"), total))
    assert context.table_test_home.pending_total().text == total

@when(u'I click the Get Approved Sum button')
def step_impl(context):
    context.table_test_home.approved_button().click()

@then(u'I can see my approved reimbursement total is {total}')
def step_impl(context, total: float):
    wait = WebDriverWait(context.driver, 1).until(text_to_be_present_in_element((By.ID, "approved-total"), total))
    assert context.table_test_home.approved_total().text == total


