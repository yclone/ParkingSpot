from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@given('I am on the login page')
async def navigate_to_login(page):
    login_page = LoginPage(page)
    await login_page.navigate()

@when(parsers.parse('I enter username "{username}" and password "{password}"'))
async def enter_credentials(page, username, password):
    login_page = LoginPage(page)
    await login_page.login(username, password)

@then('I should be redirected to the dashboard')
async def verify_dashboard(page):
    dashboard_page = DashboardPage(page)
    assert await dashboard_page.is_dashboard_visible()

@then('I should see an error message')
async def verify_error_message(page):
    error_message = page.locator('.error-message')
    assert await error_message.is_visible()
