Feature: Temperature conversion

  Scenario: Converting Fahrenheit to Celsius
    Given the Fahrenheit temperature is 32F
    When the temperature is converted to Celsius
    Then the temperature should be 0C


  Scenario: Converting Celsius to Fahrenheit
    Given the Celsius temperature is 100C
    When the temperature is converted to Fahrenheit
    Then the temperature should be 212F

