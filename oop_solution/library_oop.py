class Book:
    def __init__(self, code, name, writer, copies_total):
        self.code = code
        self.name = name
        self.writer = writer
        self.copies_total = copies_total
        self.copies_left = copies_total

    def borrow_copy(self):
        if self.copies_left > 0:
            self.copies_left -= 1
            return True
        return False

    def return_copy(self):
        if self.copies_left < self.copies_total:
            self.copies_left += 1
            return True
        return False
