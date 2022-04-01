Feature: I can log in to my account on the reimbursement website

  Scenario Outline:
    Given I am on the Log In home page
    When  I enter <employeeUsername> into the input bar
    When  I type out <employeePassword> into my input bar
    When  I click the Submit button
    Then  I should be on a page with the title Home Screen



    Examples:
      | employeeUsername | employeePassword |  |
      | AGator           | Password         |  |
