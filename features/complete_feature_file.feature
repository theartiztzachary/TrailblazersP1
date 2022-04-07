Feature: I can log in to my account on the reimbursement website and see my reimbursement history, submit a new reimbursement, and cancel pending reimbursements

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    Then I should be on the employee home page

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
    When I am on the employee home page
    Then I can see the first entry ID is <reimbursement_id>

    Examples:
      | employeeUsername | employeePassword | reimbursement_id |
      | AGator           | Password         | 3                |
      | AGator2          | Password2        | 7                |
      | SEagle           | Password3        | 4                |

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    When I am on the employee home page
    Then I can see my pending reimbursement total is <total>

    Examples:
      | employeeUsername | employeePassword | total   |
      | AGator           | Password         | 2870.59 |
      | AGator2          | Password2        | 1172.49 |
      | SEagle           | Password3        | 401.4   |

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    When I am on the employee home page
    Then I can see my approved reimbursement total is <total>

    Examples:
      | employeeUsername | employeePassword | total  |
      | AGator           | Password         | 140    |
      | AGator2          | Password2        | 61.22  |
      | SEagle           | Password3        | 450.76 |

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    When I am on the employee home page
    When I click the Submit Reimbursement button
    When I am on the Submit Reimbursement page
    When I enter <amount> in the Amount textbox
    When I enter <reason>  in the Reason textbox
    When I enter <reimbursementComment> in the Reimbursement Comment textbox
    When I click Submit button
    When I see an alert
    When I accept the alert
    Then I should be on the employee home page

    Examples:
      | employeeUsername | employeePassword | amount | reason | reimbursementComment |
      | SDragon          | Password6        | 18.12  | gas    | Meet Client          |
      | SDragon          | Password6        | 108.00 | hotel  | Stayed at Marriott   |
      | SDragon          | Password6        | 703.01 | hotel  | stayed at the dury   |

  Scenario Outline:
    Given I am on the Log In home page
    When I enter <employeeUsername> into the input bar
    When I type out <employeePassword> into my input bar
    When I click the login button
    When I am on the employee home page
    When I click on the cancel reimbursement link
    When I should be on the cancel reimbursement home page
    When I enter <reimbursement_id> into the text box
    When I click the submit button
    When I see an alert
    When I accept the alert
    Then I should be on the employee home page

    Examples:
      | employeeUsername | employeePassword | reimbursement_id |
      | SDragon          | Password6        | 80               |
      | SDragon          | Password6        | 81               |
      | SDragon          | Password6        | 82               |