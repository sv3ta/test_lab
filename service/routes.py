from flask import Blueprint, request, jsonify
from models import Product
from database import db

product_bp = Blueprint('products', __name__)


@product_bp.route('', methods=['GET'])
def list_products():
    query = Product.query

    name = request.args.get('name')
    category = request.args.get('category')
    availability = request.args.get('availability')

    if name:
        query = query.filter(Product.name.ilike(f'%{name}%'))
    if category:
        query = query.filter_by(category=category)
    if availability is not None:
        query = query.filter_by(availability=availability == 'true')

    return jsonify([p.to_dict() for p in query.all()])


@product_bp.route('/<int:product_id>', methods=['GET'])
def read_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())


@product_bp.route('', methods=['POST'])
def create_product():
    data = request.json
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201


@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.json
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return jsonify(product.to_dict())


@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return '', 204