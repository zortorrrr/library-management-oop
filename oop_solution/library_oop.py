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

class Library:
    def __init__(self):
        self.books = []
        self.members = []   
        self.loan_records = [] 

    def add_book(self, code, name, writer, copies_total):
        if any(b.code == code for b in self.books):
            print(f"[!] Book code {code} already exists.")
            return False

        book = Book(code, name, writer, copies_total)
        self.books.append(book)
        print(f"[+] Added '{book.name}' by {book.writer}")
        return True

    def find_book(self, book_code):
        for bk in self.books:
            if bk.code == book_code:
                return bk
        return None

    def add_member(self, ident, nickname, contact="N/A"):
        if any(m.ident == ident for m in self.members):
            print(f"[!] Member {ident} already exists.")
            return False

        member = Member(ident, nickname, contact)
        self.members.append(member)
        print(f"[+] Registered member: {member.nickname}")
        return True

    def find_member(self, member_code):
        for mb in self.members:
            if mb.ident == member_code:
                return mb
        return None

    def borrow_book(self, member_code, book_code):
        member = self.find_member(member_code)
        book = self.find_book(book_code)

        if not member:
            print("[!] Borrow failed: member not found")
            return False
        if not book:
            print("[!] Borrow failed: book not found")
            return False

        if member.borrow_book(book):
            self.loan_records.append({
                "member_id": member.ident,
                "member_name": member.nickname,
                "book_id": book.code,
                "book_name": book.name
            })
            return True

        return False

    def return_book(self, member_code, book_code):
        member = self.find_member(member_code)
        book = self.find_book(book_code)

        if not member or not book:
            print("[!] Return failed: member/book missing")
            return False

        if member.return_book(book):
            self.loan_records = [
                entry for entry in self.loan_records
                if not (entry["member_id"] == member.ident and entry["book_id"] == book.code)
            ]
            return True

        return False

    def display_available_books(self):
        print("\n=== Available Books ===")
        any_book = False
        for bk in self.books:
            if bk.copies_left > 0:
                any_book = True
                print(f"{bk.name} by {bk.writer} — {bk.copies_left} left")
        if not any_book:
            print("(none)")

    def display_member_books(self, member_code):
        member = self.find_member(member_code)
        if not member:
            print("[!] Member not found")
            return

        print(f"\n=== Items borrowed by {member.nickname} ===")
        if member.items_on_loan:
            for vol in member.items_on_loan:
                print(f"- {vol.name} by {vol.writer}")
        else:
            print("(no items borrowed)")
