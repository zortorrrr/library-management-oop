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
