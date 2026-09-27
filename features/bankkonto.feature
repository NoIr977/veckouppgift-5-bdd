Feature: Bank account

Scenario: Empty bank account

Given a new bank account is created
Then the account balance should be 0

Scenario Outline: Put the money to the bank account

Given a new bank account is created
When <increased_amount> is deposited into the account
Then the account balance should be <expected_amount>

Examples:
  |increased_amount|expected_amount|
  |   100          | 100           |
  |   250          | 250           |
  |   500          | 500           |


Scenario Outline: Withdraw money

Given a new bank account is created
When <deposit_amount> is deposited into the account
And <withdraw_amount> is withdrawn from the account
Then the account balance should be <expected_amount>

Examples:

  |deposit_amount| withdraw_amount | expected_amount|
  | 500          | 100             | 400            |


Scenario Outline: Apply interest

Given a new bank account is created
When <deposit_amount> is deposited into the account
And 5 percent interest is applied
Then the account balance should be <expected_amount>

Examples:

  | deposit_amount | expected_amount|
  | 100            | 105            |
  | 200            | 210            |

Scenario Outline: Transfer the money between accounts

Given two bank accounts are created
And the first account has <first_amount>
And the second account has <second_amount>
When <transfer_amount> is transferred from the first account to the second account
Then the first account balance should be <expected_first>
And the second account balance should be <expected_second>

Examples:
  |first_amount    |second_amount  | transfer_amount| expected_first| expected_second|
  |   300          | 200           | 100            |  200          | 300            |
  |   250          | 150           | 50             |  200          | 200            |
  |   700          | 500           | 150            | 550           | 650            |
