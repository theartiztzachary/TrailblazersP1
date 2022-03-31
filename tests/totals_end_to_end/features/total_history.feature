Feature: I can get my reimbursement history by inputting my employee ID

  Scenario Outline:
    Given I am on the reimbursement home page
    When I enter <employee_id> into the input bar
    When I click the Get History button
    Then I can see my full reimbursement history

  Scenario Outline:
    Given I am on the reimbursement home page
    When I enter <employee_id> into the input bar
    When I click the Get Pending Sum button
    Then I can see my pending reimbursement total is <total>



  Scenario Outline:
    Given I am on the reimbursement home page
    When I enter <employee_id> into the input bar
    When I click the Get Approved Sum button
    Then I can see my approved reimbursement total is <total>

    Examples:
      | employee_id | total |
      | 1           | 215   |