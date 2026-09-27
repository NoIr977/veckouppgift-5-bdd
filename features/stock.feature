Feature: Stock tests

Scenario Outline:Adding a product to stock

Given the stock is empty
When a product <name> with <amount> is added to the stock
Then the product <name> is in the stock
And the amount is <amount>

Examples:
  |name   |amount|
  |apple  |5     |
  |sugar  |3     |
  |cabbage|8     |


Scenario Outline: Decreasing amount of a product

Given the product <name> with amount <initial_amount> is in the stock
When decreasing amount <decreased_amount> of a product <name>
Then the amount should be <expected_amount>

Examples:
  |name   |initial_amount|decreased_amount|expected_amount|
  |apple  |5             |2               |3              |
  |sugar  |3             |1               |2              |
  |cabbage|8             |5               |3              |
