Feature: Checkout process

  Scenario: Complete checkout after adding products
    Given I am logged in with valid credentials
    When I add products to the cart
    And I go to the cart and proceed to checkout
    And I fill in my personal information
    And I finish the checkout
    Then I should see the confirmation message "Thank you for your order!"