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

class Member:
    def __init__(self, ident, nickname, contact="N/A"):
        self.ident = ident
        self.nickname = nickname
        self.contact = contact
        self.items_on_loan = [] 

    def borrow_book(self, volume):
        if len(self.items_on_loan) >= 3:
            print("Limit reached: cannot borrow more than 3 items!")
            return False

        if not volume.borrow_copy():
            print("Unavailable: no remaining copies to borrow.")
            return False

        self.items_on_loan.append(volume)
        print(f"{self.nickname} has checked out '{volume.name}'")
        return True

    def return_book(self, volume):
        if volume not in self.items_on_loan:
            print("Return error: this item is not in the member's loan list.")
            return False

        self.items_on_loan.remove(volume)
        volume.return_copy()
        print(f"{self.nickname} returned '{volume.name}' successfully")
        return True
