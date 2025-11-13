from library_oop import Book, Member


print("### MEMBER CLASS DEMONSTRATION ###\n")


member_a = Member(202, "Brian Torres", "brian.torres@domain.com")
bk1 = Book(11, "Automate the Boring Stuff", "Al Sweigart", 3)
bk2 = Book(12, "Fluent Python", "Luciano Ramalho", 2)

print("Member Details")
print(" ID :", member_a.id)
print(" Name :", member_a.name)
print(" Email :", member_a.email)
print(" Borrowed count =", len(member_a.borrowed_books))


print("\nBorrowing available books ...")
for b in (bk1, bk2):
    member_a.borrow_book(b)
    print(f"✓ Borrowed '{b.title}'")

print("\nCurrently borrowed:")
for book in member_a.borrowed_books:
    print("  -", book.title)


print("\nTrying to borrow additional titles ...")
bk3 = Book(13, "Effective Java", "Joshua Bloch", 1)
bk4 = Book(14, "Clean Architecture", "Robert C. Martin", 1)

for item in (bk3, bk4):
    member_a.borrow_book(item)
    print("→ Borrowed:", item.title)

print("\nTotal borrowed so far:", len(member_a.borrowed_books))

print("\nReturning one book ...")
member_a.return_book(bk1)
print("After returning, books left:")
for remain in member_a.borrowed_books:
    print(f"  * {remain.title}")

print("\nAttempting to return a book already returned ...")
member_a.return_book(bk1)
