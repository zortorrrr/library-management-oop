from library_oop import Book, Member

print("=== TESTING CLASS: Member ===")

m1 = Member(501, "Kurisu Makise", "kurisu@futurelab.jp")

b1 = Book(21, "Steins;Gate: The Committee of 300", "Chiyomaru Shikura", 2)
b2 = Book(22, "A Certain Magical Index", "Kazuma Kamachi", 1)

print("\n--- Member info ---")
print(f"ID: {m1.ident}")
print(f"Name: {m1.nickname}")
print(f"Email: {m1.contact}")
print(f"Borrowed books: {len(m1.items_on_loan)}")

print("\n--- Borrowing books ---")
m1.borrow_book(b1)
m1.borrow_book(b2)

print(f"Books borrowed by {m1.nickname}:")
for volume in m1.items_on_loan:
    print(f"  - {volume.name}")

print("\n--- Trying to borrow more than 3 books ---")
b3 = Book(23, "Re:Zero Arc 1", "Tappei Nagatsuki", 1)
b4 = Book(24, "The Melancholy of Haruhi Suzumiya", "Nagaru Tanigawa", 1)

m1.borrow_book(b3)
m1.borrow_book(b4)

print(f"\nBorrowed books count: {len(m1.items_on_loan)}")

print("\n--- Returning a book ---")
m1.return_book(b1)

print("Books remaining after return:")
for volume in m1.items_on_loan:
    print(f"  - {volume.name}")

print("\n--- Returning a book not borrowed ---")
m1.return_book(b1)
