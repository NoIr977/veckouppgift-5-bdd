from behave import given, when, then
from src.bank import BankAccount


@given("a new bank account is created")
def step_bank_account_created(context):
    context.account = BankAccount()


@when("{increased_amount:d} is deposited into the account")
def step_deposit(context, increased_amount):
    context.account.add_money(increased_amount)


@when("{withdraw_amount:d} is withdrawn from the account")
def step_withdraw(context, withdraw_amount):
    context.account.withdraw(withdraw_amount)


@when("5 percent interest is applied")
def step_interest(context):
    context.account.apply_interest()


@then("the account balance should be {expected:d}")
def step_check_balance(context, expected):
    assert context.account.balance == expected


@given("two bank accounts are created")
def step_two_accounts(context):
    context.account1 = BankAccount()
    context.account2 = BankAccount()


@given("the first account has {amount:d}")
def step_first_account(context, amount):
    context.account1.add_money(amount)


@given("the second account has {amount:d}")
def step_second_account(context, amount):
    context.account2.add_money(amount)


@when("{amount:d} is transferred from the first account to the second account")
def step_transfer(context, amount):
    context.account1.transfer(context.account2, amount)


@then("the first account balance should be {expected:d}")
def step_check_first(context, expected):
    assert context.account1.balance == expected


@then("the second account balance should be {expected:d}")
def step_check_second(context, expected):
    assert context.account2.balance == expected