from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

@given('I am logged in with valid credentials')
def step_login(context):
    context.page = context.browser.new_page()
    context.login_page = LoginPage(context.page)
    context.login_page.navigateTo()
    context.login_page.enter_username(context.username)
    context.login_page.enter_password(context.password)
    context.login_page.click_login()
    context.inventory_page = InventoryPage(context.page)

@when('I add products to the cart')
def step_add_products(context):
    context.inventory_page.add_to_cart(context.product_1)
    context.inventory_page.add_to_cart(context.product_2)

@when('I go to the cart and proceed to checkout')
def step_go_to_checkout(context):
    context.inventory_page.go_to_cart()
    context.checkout_page = CheckoutPage(context.page)
    context.checkout_page.click_checkout()

@when('I fill in my personal information')
def step_fill_info(context):
    context.checkout_page.enter_checkout_info(
        context.first_name,
        context.last_name,
        context.postal_code
    )

@when('I finish the checkout')
def step_finish_checkout(context):
    context.checkout_page.finish_checkout()

@then('I should see the confirmation message "Thank you for your order!"')
def step_check_confirmation(context):
    assert context.checkout_page.get_confirmation_text() == "Thank you for your order!"