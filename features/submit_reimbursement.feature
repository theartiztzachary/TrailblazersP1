Feature: I can submit reimbursement request using this page

  Scenario Outline:
    Given I am on the Submit Reimbursement page
    When  I enter <employeeId> in the EmployeeId textbox
    When  I enter <amount> in the Amount textbox
    When  I enter <reason>  in the Reason textbox
    When  I enter <reimbursementComment> in the Reimbursement Comment textbox
    When  I click Submit button
    Then  I should be on the Reimbursement home page



    Examples:
      | employeeId | amount | reason | reimbursementComment     |
      | 1          | 100.23 | dining | Had dinner with Customer |