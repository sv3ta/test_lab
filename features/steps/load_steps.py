from behave import given
from models import Product
from database import db


@given('the system has products')
def step_load_initial_data(context):
    db.session.query(Product).delete()

    products = [
        Product(name='Laptop', category='Electronics', availability=True),
        Product(name='Headphones', category='Electronics', availability=False)
    ]

    for product in products:
        db.session.add(product)

    db.session.commit()