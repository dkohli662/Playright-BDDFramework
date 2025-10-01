Feature: Products Page functionality
  As a user
  I want to view and interact with products
  So that I can shop successfully

  Scenario: Navigate to products page after login
    Given the user logs in with "newtest231@yopmail.com" and "Test@123"
    When the user clicks on the "Products" link
    Then the user should be navigated to the products page
    And the page should display a company logo
    And the page should display a list of products
    And the page should display a count of products

  Scenario: View product details
    Given products are visible
    When the user clicks on “View Product” for a product
    Then the user should be on a product detail page

  Scenario: Add a product from the products grid
    Given the product list is visible
    When the user hovers over a product and clicks "Add to cart"
    Then a modal “Added!” or confirmation should appear
    And the user can click on “Continue Shopping”

  Scenario: Search for an existing product
    Given the user is on the All Products page
    When the user enters “top” in the product search box and clicks “Search”
    Then the “SEARCHED PRODUCTS” section should be shown
    And every displayed product in results should match or contain “top”

  Scenario: Add multiple products to cart
    Given the product list is visible
    When the user adds 4 products via Add to cart
    And clicks Cart button
    Then the cart page should list those products






