import pytest
from app import app, library  # Import the app and shared library instance

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Reset the library state before each test
        library.books.clear()
        library.members.clear()
        yield client

# Book APIs
def test_add_book(client):
    response = client.post('/books', json={
        'book_id': 1,
        'title': 'Test Book',
        'author': 'Test Author',
        'year': 2020
    })
    assert response.status_code == 201
    assert b"Book added successfully!" in response.data

def test_get_books(client):
    client.post('/books', json={
        'book_id': 1,
        'title': 'Test Book',
        'author': 'Test Author',
        'year': 2020
    })
    response = client.get('/books')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_book(client):
    client.post('/books', json={
        'book_id': 1,
        'title': 'Test Book',
        'author': 'Test Author',
        'year': 2020
    })
    response = client.get('/books/1')
    assert response.status_code == 200
    assert response.json['title'] == 'Test Book'

def test_update_book(client):
    client.post('/books', json={
        'book_id': 1,
        'title': 'Test Book',
        'author': 'Test Author',
        'year': 2020
    })
    response = client.put('/books/1', json={'title': 'Updated Test Book'})
    assert response.status_code == 200
    response = client.get('/books/1')
    assert response.json['title'] == 'Updated Test Book'

def test_delete_book(client):
    client.post('/books', json={
        'book_id': 1,
        'title': 'Test Book',
        'author': 'Test Author',
        'year': 2020
    })
    response = client.delete('/books/1')
    assert response.status_code == 200
    assert b"Book deleted successfully!" in response.data

    # Verify the book is deleted
    response = client.get('/books/1')
    assert response.status_code == 404

# Member APIs
def test_add_member(client):
    response = client.post('/members', json={
        'member_id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    assert b"Member added successfully!" in response.data

def test_get_members(client):
    client.post('/members', json={
        'member_id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    response = client.get('/members')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_member(client):
    client.post('/members', json={
        'member_id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    response = client.get('/members/1')
    assert response.status_code == 200
    assert response.json['name'] == 'John Doe'

def test_update_member(client):
    client.post('/members', json={
        'member_id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    response = client.put('/members/1', json={'name': 'Jane Doe'})
    assert response.status_code == 200
    response = client.get('/members/1')
    assert response.json['name'] == 'Jane Doe'

def test_delete_member(client):
    client.post('/members', json={
        'member_id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    response = client.delete('/members/1')
    assert response.status_code == 200
    assert b"Member deleted successfully!" in response.data

    # Verify the member is deleted
    response = client.get('/members/1')
    assert response.status_code == 404
