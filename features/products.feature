Feature: Product Management

Scenario: List all products
  Given the system has products
  When I list all products
  Then I should see multiple products

Scenario: Search products by name
  Given the system has products
  When I search for product by name
  Then I should see matching products

Scenario: Search products by category
  Given the system has products
  When I search for products in a category
  Then I should see products in that category

Scenario: Search products by availability
  Given the system has products
  When I search for available products
  Then I should see only available products

Scenario: Create a product
  When I create a new product
  Then the product should be created successfully

Scenario: Update a product
  Given the system has products
  When I update a product
  Then the product should be modified

Scenario: Delete a product
  Given the system has products
  When I delete a product
  Then the product should be removed