Feature: I can submit reimbursement request using this page

  Scenario Outline:
    Given I am on the Submit Reimbursement page
    When  I enter <employeeId> in the EmployeeId textbox
    When  I enter <amount> in the Amount textbox
    When  I enter <reason>  in the Reason textbox
    When  I enter <reimbursementComment> in the Reimbursement Comment textbox
    Then  I click Submit button


    Examples:
      | employeeId | amount | reason | reimbursementComment |
      | 1          | 18.23  | gas    | Meet Client          |
      | 2          | 108.00 | Hotel  | Stayed at Marriott   |