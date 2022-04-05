from behave import given, when, then


@given(u'I am on the cancel reimbursement home page')
def step_impl(context):
    context.driver.get("C:\Users\Tashawn\Desktop\TrailblazersP1\cancel_reimbursement_home_page(for_fetch()).html")


@when(u'I enter {reimbursement_id} into the text box')
def step_impl(context, reimbursement_id: int):
    context.employee_home_page.reimbursement_id().send_keys(reimbursement_id)


@then(u'I should be on a page with the title {title}')
def step_impl(context, title: str):
    assert context.driver.title == title
