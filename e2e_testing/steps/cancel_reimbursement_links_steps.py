from behave import given, when, then


@given(u'I am on the employee home page')
def step_impl(context):
    # context.driver.get("employee-home-page.html")
    context.driver.get("file:///C:/Users/Tashawn/Desktop/TrailblazersP1/employee_home_page.html")


@when(u'I click on the cancel reimbursement option')
def step_impl(context):
    context.driver.get("http://localhost:63342/TrailblazersP1/cancel_reimbursement_home_page(for_fetch("
                       ")).html?_ijt=61s5gvbsq52a5et8ea206qvmko")


@when(u'I click the submit button')
def step_impl(context):
    context.driver.submit_button().click()


@then(u'I should be on the cancel reimbursement main page')
def step_impl(context):
    assert context.driver.title == "Cancel Reimbursement"
