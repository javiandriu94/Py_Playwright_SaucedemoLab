from behave import given, when, then
from pages.login_page import LoginPage

@given('I am on the login page')
def step_open_login_page(context):
    context.page = context.browser.new_page()
    context.login_page = LoginPage(context.page)
    context.login_page.navigateTo()

@when('I enter valid username and password')
def step_enter_credentials(context):
    context.login_page.enter_username(context.username)
    context.login_page.enter_password(context.password)

@when('I click the login button')
def step_click_login(context):
    context.login_page.click_login()

@then('I should see the inventory page')
def step_check_inventory(context):
    assert "inventory" in context.page.url