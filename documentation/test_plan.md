# Test Plan Document

##Technologies Used
- Languages: Python, PostgreSQL
- Packages: PsycoPG[Binary], Pytest, Flask
- IDE: PyCharm
- Tertiary Programs: DBeaver, Postman, AWS Database, AWS E2, GitHub, GitBash, Zoom, Discord, [front end placeholder :)]]

##Deadlines

###Sprint 1 End: March 25, 2022

###Sprint 2 End: April 1st, 2022

###Sprint 3 End: April 7th, 2022

###Final Deadline: April 8th, 2022

##What Is Being Tested
###Test Suite - Data Access Layer
####"Positive" Tests
- Test that when you select a username from the database, it returns the password.
- Test that when you select a given employee by their employee ID, it returns the reimbursement data associated with them.
- Test that when a new reimbursement request is made, it is put into the database.
- Test that when you select a reimbursement ID from the database, it returns itself.
- Test that when a reimbursement request is updated, its status code is updated in the database.
- Test that when the sum of all completed reimbursements is queried, it returns the correct sum.
- Test that when the sum of all pending reimbursements is queried, it returns the correct sum.

####"Negative" Tests
- Test that when you give a username that does not exist, an empty return is passed up to the service layer.
- Test that when you give a reimbursement ID that does not exist, an empty return is passed up to the service layer.

###Test Suite - Service Layer
####Positive Tests
- Test that when you give a username and password, there is no error. (Mocked)
- Test that when you give the correct information for a reimbursement request, there is no error. (Mocked)
- Test that numeric strings are typecast correctly. (Stubbed)
- Test that when you give the correct reimbursement ID to cancel the reimbursement, there is no error. (Mocked)

####Negative Tests
- Test that when you give a username that does not exist, an error is raised. (Mocked)
- Test that when you give a password that does not match the username, an error is raised. (Mocked)
- Test that when you give non-numeric strings, you get an error. 
- Test that when you give a number outside the business rules range (1 - 1000), an error is raised.
- Test that when you give a number with more than two decimal points, an error is raised.
- Test that when you give a comment that is more than 100 characters, an error is raised.
- Test that when you give a reimbursement ID that does not exist, an error is raised. (Mocked)

###Test Suite - API Layer
####Positive Tests
- Test that when you give the correct username and password, you get a success code. (Specifics will be given when we get to front end development.)
- Test that when you give the correct information for a reimbursement request, you get a success code. (Specifics will be given when we get to front end development).
- Test that when you give the correct reimbursement ID to cancel the reimbursement, you get a success code. (Specifics will be given when we get to front end development.)
- Test that when you ask for the sum of completed reimbursements, you get a success code. (Specifics will be given when we get to front end development.)
- Test that when you ask for the sum of pending reimbursements, you get a success code. (Specifics will be given when we get to front end development.)

####Negative Tests
- Test that when you give an incorrect username, you get a fail code. (Specifics will be given when we get to front end development.)
- Test that when you give an incorrect password, you get a fail code. (Specifics will be given when we get to front end development.)
- Test that when you give non-numeric strings, you get a fail code. (Specifics will be given when we get to front end development.)
- Test that when you give a number outside the business rules range (1 - 1000), you get a fail code. (Specifics will be given when we get to front end development.)
- Test that when you give a number with more than two decimal points, you get a fail code. (Specifics will be given when we get to front end development.)
- Test that when you give a comment that is more than 100 characters, you get a fail code. (Specifics will be given when we get to front end development.)
- Test that when you give a reimbursement ID that does not exist, you get a fail code. (Specifics will be given when we get to front end development.) 

###Test Suite - Front End
This will be filled out after we are introduced to them in class.
(Login)
(Logout)
(Submit Reimbursement)
(Cancel Reimbursement)
(Total Reimbursed)

##What Is Not Being Tested
- Do not test for if the given username or password is a string or not, because the front end should be sending these inputs as strings to the system.
- Do not test the data type of the reason, because the front end should be sending these inputs as strings to the system.
- Do not test validations for sum of completed and/or pending reimbursements because those functions are handled without user input.