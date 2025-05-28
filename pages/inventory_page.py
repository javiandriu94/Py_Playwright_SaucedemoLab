class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self, product_name):
        locator = self.page.locator(f"text={product_name}").locator("..").locator("button")
        locator.click()

    def go_to_cart(self):
        self.page.click("#shopping_cart_container")
