from flask import Flask, request, jsonify
from models import Library, Book, Member

app = Flask(__name__)
library = Library()

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = Book(
        book_id=data['book_id'],
        title=data['title'],
        author=data['author'],
        year=data['year']
    )
    library.add_book(book)
    return jsonify({"message": "Book added successfully!"}), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = library.get_books()
    return jsonify([{
        'book_id': book.book_id,
        'title': book.title,
        'author': book.author,
        'year': book.year
    } for book in books])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id: int):
    book = library.get_book_by_id(book_id)
    if not book:
        return jsonify({"message": "Book not found!"}), 404
    return jsonify({
        'book_id': book.book_id,
        'title': book.title,
        'author': book.author,
        'year': book.year
    })

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id: int):
    data = request.get_json()
    updated = library.update_book(
        book_id, 
        title=data.get('title'), 
        author=data.get('author'), 
        year=data.get('year')
    )
    if updated:
        return jsonify({"message": "Book updated successfully!"})
    return jsonify({"message": "Book not found!"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id: int):
    deleted = library.delete_book(book_id)
    if deleted:
        return jsonify({"message": "Book deleted successfully!"})
    return jsonify({"message": "Book not found!"}), 404

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    member = Member(
        member_id=data['member_id'],
        name=data['name'],
        email=data['email']
    )
    library.add_member(member)
    return jsonify({"message": "Member added successfully!"}), 201

@app.route('/members', methods=['GET'])
def get_members():
    members = library.get_members()
    return jsonify([{
        'member_id': member.member_id,
        'name': member.name,
        'email': member.email
    } for member in members])

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id: int):
    member = library.get_member_by_id(member_id)
    if not member:
        return jsonify({"message": "Member not found!"}), 404
    return jsonify({
        'member_id': member.member_id,
        'name': member.name,
        'email': member.email
    })

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id: int):
    data = request.get_json()
    updated = library.update_member(
        member_id,
        name=data.get('name'),
        email=data.get('email')
    )
    if updated:
        return jsonify({"message": "Member updated successfully!"})
    return jsonify({"message": "Member not found!"}), 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id: int):
    deleted = library.delete_member(member_id)
    if deleted:
        return jsonify({"message": "Member deleted successfully!"})
    return jsonify({"message": "Member not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
