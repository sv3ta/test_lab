from app import create_app
from models import Product
from tests.factories import ProductFactory


def test_list_products():
    app = create_app()
    client = app.test_client()

    with app.app_context():
        ProductFactory.create_batch(3)
        response = client.get('/products')
        assert response.status_code == 200
        assert len(response.json) >= 3


def test_read_product():
    app = create_app()
    client = app.test_client()

    with app.app_context():
        product = ProductFactory()
        response = client.get(f'/products/{product.id}')
        assert response.status_code == 200
        assert response.json['name'] == product.name


def test_create_product():
    app = create_app()
    client = app.test_client()

    product_data = {
        'name': 'New Product',
        'category': 'Test',
        'availability': True
    }
    response = client.post('/products', json=product_data)
    assert response.status_code == 201
    assert response.json['name'] == 'New Product'


def test_update_product():
    app = create_app()
    client = app.test_client()

    with app.app_context():
        product = ProductFactory()
        update_data = {'name': 'Updated Product'}
        response = client.put(f'/products/{product.id}', json=update_data)
        assert response.status_code == 200
        assert response.json['name'] == 'Updated Product'


def test_delete_product():
    app = create_app()
    client = app.test_client()

    with app.app_context():
        product = ProductFactory()
        response = client.delete(f'/products/{product.id}')
        assert response.status_code == 204


def test_list_by_name():
    app = create_app()
    client = app.test_client()

    with app.app_context():
        ProductFactory(name='Search Product')
        response = client.get('/products?name=Search')
        assert response.status_code == 200
        assert any('Search' in product['name'] for product in response.json)


def test_list_by_category():
    app = create_app()
    client = app.test_client()

    with app.app_context():
        ProductFactory(category='Electronics')
        response = client.get('/products?category=Electronics')
        assert response.status_code == 200
        assert all(product['category'] == 'Electronics' for product in response.json)


def test_list_by_availability():
    app = create_app()
    client = app.test_client()

    with app.app_context():
        ProductFactory(availability=False)
        response = client.get('/products?availability=false')
        assert response.status_code == 200
        assert all(product['availability'] is False for product in response.json)