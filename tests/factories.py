import factory
from models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    category = factory.Faker('word')
    availability = factory.Faker('boolean')
    price = factory.Faker('pyfloat', positive=True)