from flask import Blueprint, jsonify, request
from .models import get_all_books, get_book, create_book, update_book, delete_book

main = Blueprint('main', __name__)

@main.route('/books', methods=['GET'])
def list_books():
    return jsonify(get_all_books())

@main.route('/books/<int:book_id>', methods=['GET'])
def get_single_book(book_id):
    book = get_book(book_id)
    return jsonify(book) if book else ('', 404)

@main.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = create_book(data)
    return jsonify(book), 201

@main.route('/books/<int:book_id>', methods=['PUT'])
def update_single_book(book_id):
    data = request.get_json()
    book = update_book(book_id, data)
    return jsonify(book) if book else ('', 404)

@main.route('/books/<int:book_id>', methods=['DELETE'])
def delete_single_book(book_id):
    if delete_book(book_id):
        return ('', 204)
    return ('', 404)
