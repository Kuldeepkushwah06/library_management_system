from typing import List, Optional

class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

class Member:
    def __init__(self, member_id: int, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email

class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.members: List[Member] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def get_books(self) -> List[Book]:
        return self.books

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return next((book for book in self.books if book.book_id == book_id), None)

    def update_book(self, book_id: int, title: Optional[str], author: Optional[str], year: Optional[int]) -> bool:
        book = self.get_book_by_id(book_id)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if year:
                book.year = year
            return True
        return False

    def delete_book(self, book_id: int) -> bool:
        book = self.get_book_by_id(book_id)
        if book:
            self.books.remove(book)
            return True
        return False

    def add_member(self, member: Member) -> None:
        self.members.append(member)

    def get_members(self) -> List[Member]:
        return self.members

    def get_member_by_id(self, member_id: int) -> Optional[Member]:
        return next((member for member in self.members if member.member_id == member_id), None)

    def update_member(self, member_id: int, name: Optional[str], email: Optional[str]) -> bool:
        member = self.get_member_by_id(member_id)
        if member:
            if name:
                member.name = name
            if email:
                member.email = email
            return True
        return False

    def delete_member(self, member_id: int) -> bool:
        member = self.get_member_by_id(member_id)
        if member:
            self.members.remove(member)
            return True
        return False
