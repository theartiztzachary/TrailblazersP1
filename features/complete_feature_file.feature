Feature: I can log in to my account on the reimbursement website and see my reimbursement history

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    Then I should be on a page with the title Home Screen

    Examples:
      | employeeUsername | employeePassword |
      | AGator           | Password         |
      | AGator2          | Password2        |
      | SEagle           | Password3        |

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    When I should be on a page with the title Home Screen
    Then I can see the first entry ID is <reimbursement_id>

    Examples: # fill out during final lockdown

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    When I should be on a page with the title Home Screen
    Then I can see my pending reimbursement total is <total>

    Examples: #fill out during final lockdown

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    When I should be on a page with the title Home Screen
    Then I can see my approved reimbursement total is <total>

    Examples: #fill out during final lockdown

  Feature: I can submit reimbursement request using this page

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    When I should be on a page with the title Home Screen
    When I click the Submit Reimbursement button
    When I am on the Submit Reimbursement page
    When  I enter <amount> in the Amount textbox
    When  I enter <reason>  in the Reason textbox
    When  I enter <reimbursementComment> in the Reimbursement Comment textbox
    Then  I click Submit button

    Examples:
      | employeeUsername | employeePassword | amount | reason | reimbursementComment |
      | SDragon          | Password6        | 18.12  | gas    | Meet Client          |
      | SDragon          | Password6        | 108.00 | Hotel  | Stayed at Marriott   |
