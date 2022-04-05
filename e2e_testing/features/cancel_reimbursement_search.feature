Feature: I can submit a reimbursement request

  Scenario Outline:
    Given I am on the cancel reimbursement home page
    When  I enter <reimbursement_id> into the text box
    When  I click the submit button
    Then  I should be on a page with the title <title>

    Examples:
      | reimbursement_id | title    |
      | 1000             | Cancel Reimbursement |

