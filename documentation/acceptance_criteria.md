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

###Scenario: As an employee, I want to log in BUT I mess up my username and/or password.
- GIVEN: I am the site home page,
- WHEN: I enter my username,
- WHEN: I enter my password but incorrectly,
- WHEN: I click the Login button,
- THEN: I get a popup that tells me my username and/or password is incorrect.

###Scenario: As an employee, I want to log out so that nobody else makes reimbursement requests in my name.
- GIVEN: I am on the reimbursement home page,
- WHEN: I click the sidebar button,
- WHEN: I click the Logout button,
- THEN: I am directed to the site home page.

###Scenario: As an employee, I want to log out BUT I don't get logged out.
- GIVEN: I am on the reimbursement home page,
- WHEN: I click the sidebar button,
- WHEN: I click the Logout button,
- THEN: I get a popup that tells me there was a server error and I was not logged out.

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

###Scenario: As an employee, I want to submit a reimbursement request BUT I entered I comment that was too long.
- GIVEN: I am on the reimbursement home page,
- WHEN: I click the sidebar button,
- WHEN: I click on the 'Begin Reimbursement' button,
- WHEN: I am directed to the reimbursement form page,
- WHEN: I click on the reimbursement reason drop down menu,
- WHEN: I select my reimbursement reason,
- WHEN: I enter a reimbursement comment,
- WHEN: I click the 'Submit Reimbursement Request' button,
- THEN: I get a popup that tells me that something was wrong with my request information and to double-check it.

###Scenario: As an employee, I want to cancel a reimbursement request so that I correct a mistake in a request I made.
- GIVEN: I am on the reimbursement home page,
- WHEN: I click on the sidebar button,
- WHEN: I click the 'Cancel Request' button,
- WHEN: I am directed to the cancel reimbursement page,
- WHEN: I enter my request number,
- WHEN: I hit an initial 'Cancel' button,
- WHEN: I am directed to a page to confirm I want to cancel,
- WHEN: I click on the 'Confirm Cancellation' button,
- THEN: I am directed to a confirmation page that confirms the request was canceled.

###Scenario: As an employee, I want to cancel a reimbursement request BUT I provide the wrong ID.
- GIVEN: I am on the reimbursement home page,
- WHEN: I click on the sidebar button,
- WHEN: I click the 'Cancel Request' button,
- WHEN: I am directed to the cancel reimbursement page,
- WHEN: I enter my request number,
- WHEN: I hit an initial 'Cancel' button,
- THEN: I get a popup that tells me that my reimbursement ID is invalid.

###Scenario: As an employee, I want to see the total amount I have requested so that I can budget.
- GIVEN: I am on the reimbursement home page,
- THEN: I can see my entire reimbursement history.

###Scenario: As an employee, I want to see the total amount I have requested BUT there is a server error.
- GIVEN: I am on the reimbursement home page,
- THEN: I am shown a 500 error.