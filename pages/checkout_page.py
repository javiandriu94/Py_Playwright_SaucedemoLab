class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def click_checkout(self):
        self.page.click("button:has-text('Checkout')")

    def enter_checkout_info(self, first_name, last_name, postal_code):
        self.page.fill('[data-test="firstName"]', first_name)
        self.page.fill('[data-test="lastName"]', last_name)
        self.page.fill('[data-test="postalCode"]', postal_code)
        self.page.click('[data-test="continue"]')

    def finish_checkout(self):
        self.page.click('[data-test="finish"]')

    def get_confirmation_text(self):
        return self.page.inner_text(".complete-header")