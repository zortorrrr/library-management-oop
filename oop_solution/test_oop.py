from library_oop import Book, Member, Library

def test_library_system():
    """Comprehensive test of all library functions"""

    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)

    library = Library()

    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    library.add_book(101, "Sword Art Online: Aincrad", "Reki Kawahara", 3)
    library.add_book(102, "Attack on Titan: Before the Fall", "Hajime Isayama", 2)
    library.add_book(103, "Re:Zero - Starting Life in Another World", "Tappei Nagatsuki", 1)
    library.add_book(104, "The Melancholy of Haruhi Suzumiya", "Nagaru Tanigawa", 2)

    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    library.add_member(201, "Kazuto Kirigaya", "kirito@aincrad.jp")
    library.add_member(202, "Mikasa Ackerman", "mikasa@survey.jp")
    library.add_member(203, "Emilia Tan", "emilia@reem.jp")

    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    library.display_available_books()

    # Test 4: Successful Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(201, 101)  # Kirito borrows SAO
    library.borrow_book(201, 102)  # Kirito borrows AOT
    library.borrow_book(202, 101)  # Mikasa borrows SAO

    # Test 5: Display Member Books
    print("\n--- TEST 5: Display Member's Books ---")
    library.display_member_books(201)
    library.display_member_books(202)
    library.display_member_books(203)

    # Test 6: Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_available_books()

    # Test 7: Borrowing Last Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    library.borrow_book(203, 103)   # Emilia borrows Re:Zero
    library.display_available_books()

    # Test 8: Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(202, 103)

    # Test 9: Borrow Limit
    print("\n--- TEST 9: Testing Borrowing Limit ---")
    library.borrow_book(201, 104)
    library.display_member_books(201)
    library.borrow_book(201, 103)  # Should fail

    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    library.return_book(201, 101)
    library.return_book(202, 101)
    library.display_member_books(201)
    library.display_available_books()

    # Test 11: Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(202, 102)

    # Test 12: Return + Re-borrow
    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(203, 103)
    library.borrow_book(202, 103)
    library.display_member_books(202)

    # Test 13: Error Handling
    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 101)  # invalid member
    library.borrow_book(201, 999)  # invalid book
    library.return_book(999, 101)  # invalid return
    library.display_member_books(999)

    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")

    for member in library.members:
        for book in member.items_on_loan:
            print(f"  {member.nickname} has '{book.name}'")

    print("\nAll Members and Their Books:")
    for member in library.members:
        print(f"\n{member.nickname} ({member.ident}):")
        if member.items_on_loan:
            for book in member.items_on_loan:
                print(f"  - {book.name}")
        else:
            print("  (No books borrowed)")

    library.display_available_books()

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_library_system()
