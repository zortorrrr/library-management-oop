class Book:

    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_copy(self):
        if self.available_copies <= 0:
            return False
        self.available_copies -= 1
        return True

    def return_copy(self):
        if self.available_copies >= self.total_copies:
            return False
        self.available_copies += 1
        return True

class Member:
    def __init__(self, id, name, email="N/A"):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = [] 

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        if not book.borrow_copy():
            print("Error: No copies available!")
            return False
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'")
        return True

    def return_book(self, book):
        if book not in self.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False
        self.borrowed_books.remove(book)
        book.return_copy()
        print(f"{self.name} returned '{book.title}'")
        return True
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []

    def add_book(self, id, title, author, total_copies):
        if any(book.book_id == id for book in self.books):
            print(f"Error: Book ID {id} already exists!")
            return
        book = Book(id, title, author, total_copies)
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def add_member(self, id, name, email="N/A"):
        if any(member.id == id for member in self.members):
            print(f"Error: Member ID {id} already exists!")
            return
        member = Member(id, name, email)
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully!")

    def find_member(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return False
        if not book:
            print("Error: Book not found!")
            return False

        if member.borrow_book(book):
            self.borrowed_books.append({
                "member_id": member.id,
                "member_name": member.name,
                "book_id": book.book_id,
                "book_title": book.title
            })
            return True
        return False

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False

        if member.return_book(book):
            self.borrowed_books = [
                t for t in self.borrowed_books
                if not (t["member_id"] == member.id and t["book_id"] == book.book_id)
            ]
            return True
        return False

    def display_available_books(self):
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        print(f"\n=== Books borrowed by {member.name} ===")
        if member.borrowed_books:
            for book in member.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books currently borrowed")
