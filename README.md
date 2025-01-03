# **Library Management System API**

A simple Flask-based API for managing books and members in a library system. The application provides endpoints for CRUD (Create, Read, Update, Delete) operations on books and members. The data is stored in memory for simplicity.

---

## **Table of Contents**
1. [How to Run the Project](#how-to-run-the-project)
2. [Endpoints](#endpoints)
3. [Design Choices](#design-choices)
4. [Assumptions and Limitations](#assumptions-and-limitations)

---

## **How to Run the Project**

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Steps to Run

1. Clone the GitHub Repository:

   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Kuldeepkushwah06/library_management_system.git
   cd library_management_system

2. Create a Virtual Environment (Optional but Recommended):
   python -m venv venv
   source venv/bin/activate (on Linux/Mac) or venv\Scripts\activate

3. Install Dependencies from requirements.txt:
   pip install -r requirements.txt

4. Run the Application:
   python app.py

5. Run Automated Tests:
   pytest tests/


## **Endpoints**

# Books Endpoints
POST /books: Add a new book.
GET /books: Get all books.
GET /books/<book_id>: Retrieve a specific book by ID.
PUT /books/<book_id>: Update an existing book.
DELETE /books/<book_id>: Delete a book.

# Members Endpoints
POST /members: Add a new member.
GET /members: Get all members.
GET /members/<member_id>: Retrieve a specific member by ID.
PUT /members/<member_id>: Update an existing member.
DELETE /members/<member_id>: Delete a member.

## **Design Choices**

# Framework:

Flask was chosen for its simplicity and ease of use, making it ideal for building small APIs quickly.
Flask is lightweight and flexible, allowing easy implementation of RESTful endpoints.
In-Memory Storage:

Data (books and members) is stored in Python dictionaries to avoid external dependencies like databases.
This allows for rapid development and testing without the need for setting up and maintaining a database.
However, this is not a persistent solution; data is lost when the server restarts.
Modular Design:

The application logic is kept in a single app.py file for simplicity.
Test cases for the API are stored separately in the tests/ directory to maintain clear structure and readability.
Automated Testing:

pytest and flask-testing are used to simulate requests to the API and verify correctness.
Tests are implemented for each CRUD operation to ensure the functionality of the endpoints.

## **Assumptions and Limitations**

# Assumptions
1. Unique IDs: Each book_id and member_id is assumed to be unique and numeric.
2. Required Fields: All required fields (e.g., title, author for books) are provided in the request body when adding or updating records.

# Limitations

1. No Persistent Storage:

Data is stored in memory and is lost when the server restarts.
For a production system, a database (e.g., SQLite, PostgreSQL) should be implemented to store data persistently.

2. Single-Threaded:

The app runs in a single-threaded mode by default and is not optimized for handling concurrent requests in a production environment.

3. Scalability:

The current design is suitable for small-scale applications and prototypes but does not scale well for large or production-grade systems.
Features like authentication, rate limiting, logging, and more complex error handling are not implemented.

4. Basic Error Handling:

Basic error handling is implemented, but more comprehensive checks (e.g., validating the request data) could be added to improve robustness.

