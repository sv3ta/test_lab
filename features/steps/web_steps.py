from behave import when, then
from app import create_app
from models import Product

def before_scenario(context, scenario):
    context.app = create_app()
    context.app.config['TESTING'] = True
    context.client = context.app.test_client()

@when('I list all products')
def step_list_products(context):
    context.response = context.client.get('/products')

@when('I search for product by name')
def step_search_by_name(context):
    context.response = context.client.get('/products?name=Laptop')

@when('I search for products in a category')
def step_search_by_category(context):
    context.response = context.client.get('/products?category=Electronics')

@when('I search for available products')
def step_search_available(context):
    context.response = context.client.get('/products?availability=true')

@when('I create a new product')
def step_create_product(context):
    context.response = context.client.post('/products', json={
        'name': 'New Product',
        'category': 'Test',
        'availability': True
    })

@when('I update a product')
def step_update_product(context):
    product = Product.query.first()
    context.response = context.client.put(f'/products/{product.id}', json={'name': 'Updated Product'})

@when('I delete a product')
def step_delete_product(context):
    product = Product.query.first()
    context.response = context.client.delete(f'/products/{product.id}')

@then('I should see multiple products')
def step_check_multiple_products(context):
    assert len(context.response.json) > 1

@then('I should see matching products')
def step_check_product_name(context):
    assert any('Laptop' in product['name'] for product in context.response.json)

@then('I should see products in that category')
def step_check_product_category(context):
    assert all(product['category'] == 'Electronics' for product in context.response.json)

@then('I should see only available products')
def step_check_available_products(context):
    assert all(product['availability'] is True for product in context.response.json)

@then('the product should be created successfully')
def step_check_product_created(context):
    assert context.response.status_code == 201
    assert context.response.json['name'] == 'New Product'

@then('the product should be modified')
def step_check_product_updated(context):
    assert context.response.status_code == 200
    assert context.response.json['name'] == 'Updated Product'

@then('the product should be removed')
def step_check_product_deleted(context):
    assert context.response.status_code == 204