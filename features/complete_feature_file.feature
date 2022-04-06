#Feature: I can log in to my account on the reimbursement website and see my reimbursement history
#
#  Scenario Outline:
#    Given I am on the Log In home page
#    When I enter <employeeUsername> into the input bar
#    When I type out <employeePassword> into my input bar
#    When I click the Submit button
#    Then I should be on a page with the title Home Screen
#
#    Examples:
#      | employeeUsername | employeePassword |
#      | AGator           | Password         |
#      | AGator2          | Password2        |
#      | SEagle           | Password3        |
#
#  Scenario Outline:
#    Given I am on the Log In home page
#    When I enter <employeeUsername> into the input bar
#    When I type out <employeePassword> into my input bar
#    When I click the Submit button
#    Then I can see the first entry ID is <reimbursement_id>
#
#    Examples: # fill out during final lockdown
#
#  Scenario Outline:
#    Given I am on the Log In home page
#    When I enter <employeeUsername> into the input bar
#    When I type out <employeePassword> into my input bar
#    When I click the Submit button
#    Then I can see my pending reimbursement total is <total>
#
#    Examples: #fill out during final lockdown
#
#  Scenario Outline:
#    Given I am on the Log In home page
#    When I enter <employeeUsername> into the input bar
#    When I type out <employeePassword> into my input bar
#    When I click the Submit button
#    Then I can see my approved reimbursement total is <total>
#
#    Examples: #fill out during final lockdown