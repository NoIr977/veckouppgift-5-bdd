from behave import given, when, then
from src.temperature import fahrenheit_to_celsius
from src.temperature import celsius_to_fahrenheit

@given("the Fahrenheit temperature is {temperature:d}F")
def step_given_fahrenheit(context,temperature):
    context.temperature = temperature

@when("the temperature is converted to Celsius")
def step_convert_to_celsius(context):
    context.result = fahrenheit_to_celsius(context.temperature)


@then("the temperature should be {expected:d}C")
def step_check_celsius(context, expected):
    assert context.result == expected


@given("the Celsius temperature is {temperature:d}C")
def step_given_celsius(context,temperature):
    context.temperature = temperature

@when("the temperature is converted to Fahrenheit")
def step_convert_to_fahrenheit(context):
    context.result = celsius_to_fahrenheit(context.temperature)

@then("the temperature should be {expected:d}F")
def step_check_fahrenheit(context,expected):
    assert context.result == expected