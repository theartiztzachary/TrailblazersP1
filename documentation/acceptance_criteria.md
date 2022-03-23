#User Stories
- As an employee, I want to log in so that I can be reimbursed for my expenses.
- As an employee, I want to log out so that nobody else makes reimbursement requests in my name.
- As en employee, I want to submit a reimbursement request so that I can get that money back.
- As an employee, I want to cancel a reimbursement request so that I correct a mistake in a request I made.
- As an employee, I want to see the total amount I have requested so that I can budget.

#Acceptance Criteria
###Scenario: As an employee, I want to log in so that I can be reimbursed for my expenses.
- GIVEN: I am the site home page,
- WHEN: I enter my username,
- WHEN: I enter my password,
- WHEN: I click the Login button,
- THEN: I am directed to my reimbursement home page.

###Scenario: As an employee, I want to log out so that nobody else makes reimbursement requests in my name.
- GIVEN: I am on the reimbursement home page,
- WHEN: I click the sidebar button,
- WHEN: I click the Logout button,
- THEN: I am directed to the site home page.

###Scenario: As en employee, I want to submit a reimbursement request so that I can get that money back.
- GIVEN: I am on the reimbursement home page,
- WHEN: I click the sidebar button,
- WHEN: I click on the 'Begin Reimbursement' button,
- WHEN: I am directed to the reimbursement form page,
- WHEN: I click on the reimbursement reason drop down menu,
- WHEN: I select my reimbursement reason,
- WHEN: I enter a reimbursement comment,
- WHEN: I click the 'Submit Reimbursement Request' button,
- THEN: I am directed to a confirmation page with a request number.

###Scenario: As an employee, I want to cancel a reimbursement request so that I correct a mistake in a request I made.
- GIVEN: I am on the reimbursement home page,
- WHEN: I click on the sidebar button,
- WHEN: I click the 'Cancel Request' button,
- WHEN: I am directed to the cancel reimbursement page,
- WHEN: I enter my request number,
- WHEN: I am directed to a page to confirm I want to cancel,
- WHEN: I click on the 'Confirm Cancellation' button,
- THEN: I am directed to a confirmation page that confirms the request was canceled.

###Scenario: As an employee, I want to see the total amount I have requested so that I can budget.
- GIVEN: I am on the reimbursement home page,
- THEN: I can see my entire reimbursement history.
