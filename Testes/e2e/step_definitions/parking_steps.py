from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@given('I am logged in as admin')
async def login_as_admin(page):
    login_page = LoginPage(page)
    await login_page.navigate()
    await login_page.login('admin', 'admin')

@when('I add a new parking spot with following details')
async def add_parking_spot(page, table):
    dashboard_page = DashboardPage(page)
    data = table[0]
    await dashboard_page.add_parking_spot(
        data['plate'],
        data['spot'],
        data['apartment'],
        data['block']
    )

@then('I should see the new parking spot in the list')
async def verify_new_parking_spot(page):
    dashboard_page = DashboardPage(page)
    parking_table = await dashboard_page.parking_spots_table.inner_text()
    assert 'ABC1234' in parking_table
