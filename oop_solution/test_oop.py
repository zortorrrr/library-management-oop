from library_oop import Book

print("=== TESTING CLASS: Book ===")

b1 = Book(7, "Re:Zero - Starting Life in Another World", "Tappei Nagatsuki", 4)

print(f"Title: {b1.name}")
print(f"Author: {b1.writer}")
print(f"Total copies: {b1.copies_total}")
print(f"Available copies: {b1.copies_left}")

print("\n--- Borrowing copies ---")
b1.borrow_copy()
b1.borrow_copy()
print(f"Available copies after 2 borrows: {b1.copies_left}")

print("\n--- Trying to borrow more than available ---")
borrow_success = b1.borrow_copy()
print(f"Borrow success? {borrow_success}")
print(f"Available copies now: {b1.copies_left}")

print("\n--- Returning a copy ---")
b1.return_copy()
print(f"Available copies after return: {b1.copies_left}")
