from models import Product
from database import db
from tests.factories import ProductFactory

def test_create_product():
    product = ProductFactory()
    db.session.add(product)
    db.session.commit()
    assert product.id is not None

def test_read_product():
    product = ProductFactory()
    db.session.add(product)
    db.session.commit()
    found_product = Product.query.get(product.id)
    assert found_product is not None

def test_update_product():
    product = ProductFactory()
    db.session.add(product)
    db.session.commit()
    product.name = 'Updated Name'
    db.session.commit()
    updated_product = Product.query.get(product.id)
    assert updated_product.name == 'Updated Name'

def test_delete_product():
    product = ProductFactory()
    db.session.add(product)
    db.session.commit()
    db.session.delete(product)
    db.session.commit()
    deleted_product = Product.query.get(product.id)
    assert deleted_product is None

def test_list_all_products():
    ProductFactory.create_batch(3)
    products = Product.query.all()
    assert len(products) >= 3

def test_find_by_name():
    product = ProductFactory(name='Test Product')
    db.session.add(product)
    db.session.commit()
    found_products = Product.query.filter(Product.name.ilike('%Test%')).all()
    assert len(found_products) > 0

def test_find_by_category():
    product = ProductFactory(category='Electronics')
    db.session.add(product)
    db.session.commit()
    found_products = Product.query.filter_by(category='Electronics').all()
    assert len(found_products) > 0

def test_find_by_availability():
    product = ProductFactory(availability=False)
    db.session.add(product)
    db.session.commit()
    unavailable_products = Product.query.filter_by(availability=False).all()
    assert len(unavailable_products) > 0