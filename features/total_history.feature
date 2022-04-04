Feature: I can get my reimbursement history by inputting my employee ID

  Scenario Outline:
    Given I am on the reimbursement home page
    When I enter <employee_id> into the input bar
    When I click the Get History button
    Then I can see the first entry ID is <reimbursement_id>

      Examples:
        | employee_id | reimbursement_id |
        | 1           | 2                |
        | 2           | 7                |

  Scenario Outline:
    Given I am on the reimbursement home page
    When I enter <employee_id> into the input bar
    When I click the Get Pending Sum button
    Then I can see my pending reimbursement total is <total>

    Examples:
      | employee_id | total   |
      | 1           | 500     |
      | 2           | 1009.18 |

  Scenario Outline:
    Given I am on the reimbursement home page
    When I enter <employee_id> into the input bar
    When I click the Get Approved Sum button
    Then I can see my approved reimbursement total is <total>

    Examples:
      | employee_id | total |
      | 1           | 215   |
      | 2           | 30.47 |
