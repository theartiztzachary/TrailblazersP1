from behave import when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_contains

@when(u'I should be on a page with the title Home Screen')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(title_contains("Trailblazers Reimbursement Systems - Home"))
    assert context.driver.title == "Trailblazers Reimbursement Systems - Home"

@then(u'I can see the first entry ID is {reimbursement_id}')
def step_impl(context, reimbursement_id: int):
    wait = WebDriverWait(context.driver, 1).until(text_to_be_present_in_element((By.ID, "0"), reimbursement_id))
    assert context.table_test_home.first_reimbursement_id().text == reimbursement_id

@then(u'I can see my pending reimbursement total is {total}')
def step_impl(context, total: float):
    wait = WebDriverWait(context.driver, 1).until(text_to_be_present_in_element((By.ID, "pending-total"), total))
    assert context.table_test_home.pending_total().text == total

@then(u'I can see my approved reimbursement total is {total}')
def step_impl(context, total: float):
    wait = WebDriverWait(context.driver, 1).until(text_to_be_present_in_element((By.ID, "approved-total"), total))
    assert context.table_test_home.approved_total().text == total


