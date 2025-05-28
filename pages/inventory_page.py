class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self, product_name):
        self.page.wait_for_selector(".inventory_item")
        product_locator = self.page.locator(".inventory_item").filter(has_text=product_name)
        product_locator.locator("button.btn_inventory").click()

    def go_to_cart(self):
        self.page.click("#shopping_cart_container")
