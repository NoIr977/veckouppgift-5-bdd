from behave import given, when, then
from src.stock import Stock, StockItem

@given("the stock is empty")
def step_empty_stock(context):
    context.stock = Stock()

@when("a product {name} with {amount:d} is added to the stock")
def step_added_to_stock(context, name, amount):
    context.product = StockItem(name, amount)
    context.stock.add_product(context.product)

@then("the product {name} is in the stock")
def step_check_product(context, name):
     assert context.product.name == name

@then("the amount is {amount:d}")
def step_check_amount(context, amount):
      assert context.product.amount == amount



@given("the product {name} with amount {initial_amount:d} is in the stock")
def step_product_in_stock(context, name, initial_amount):
    context.stock = Stock()
    context.product = StockItem(name,initial_amount)
    context.stock.add_product(context.product)

@when("decreasing amount {decreased_amount:d} of a product {name}")
def step_product_is_decreased(context, name,decreased_amount):
    context.stock.decrease_product(context.product,decreased_amount)

@then("the amount should be {expected_amount:d}")
def step_check_product_amount(context,expected_amount):
    assert context.product.amount == expected_amount