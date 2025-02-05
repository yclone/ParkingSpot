class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.parking_spots_table = page.locator('table')
        self.add_parking_button = page.locator('button:has-text("Add Parking Spot")')

    async def is_dashboard_visible(self):
        return await self.parking_spots_table.is_visible()

    async def add_parking_spot(self, plate, spot, apartment, block):
        await self.add_parking_button.click()
        await self.page.fill('[name="vehicle_plate"]', plate)
        await self.page.fill('[name="spot_number"]', spot)
        await self.page.fill('[name="apartment"]', apartment)
        await self.page.fill('[name="block"]', block)
        await self.page.click('button:has-text("Save")')
