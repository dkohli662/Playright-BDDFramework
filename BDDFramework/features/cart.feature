Feature: Manage items in cart

  Background:
    Given user is logged in with valid credentials
    And user has added products to cart

  Scenario: Verify products are displayed correctly in cart
      When user click on cart button
      Then all added products should be listed in the cart
      And each product should display correct name, price, quantity, and total



