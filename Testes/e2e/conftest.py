import pytest
from playwright.async_api import async_playwright
from pytest_bdd import given, when, then, parsers

@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        yield browser
        await browser.close()

@pytest.fixture
async def page(browser):
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await page.close()
    await context.close()
