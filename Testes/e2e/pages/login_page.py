class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator('[name="username"]')
        self.password_input = page.locator('[name="password"]')
        self.login_button = page.locator('button:has-text("Login")')

    async def navigate(self):
        await self.page.goto('http://localhost:5000')

    async def login(self, username, password):
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.login_button.click()
