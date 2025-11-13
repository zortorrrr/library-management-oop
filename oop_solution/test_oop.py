from library_oop import Library
library = Library()
print("=== TESTING CLASS: Library ===")


print("\n--- Adding Books ---")
library.add_book(101, "Your Name", "Makoto Shinkai", 3)
library.add_book(102, "Attack on Titan", "Hajime Isayama", 2)
library.add_book(103, "Demon Slayer: Kimetsu no Yaiba", "Koyoharu Gotouge", 1)


print("\n--- Adding Members ---")
library.add_member(301, "Naruto Uzumaki", "naruto@konoha.jp")
library.add_member(302, "Mikasa Ackerman", "mikasa@survey.jp")


print("\n--- Display Available Books ---")
library.display_available_books()


print("\n--- Borrowing Books ---")
library.borrow_book(301, 101)
library.borrow_book(301, 102)
library.borrow_book(302, 101)


print("\n--- Display Member Books ---")
library.display_member_books(301)
library.display_member_books(302)


print("\n--- Available Books After Borrowing ---")
library.display_available_books()


print("\n--- Returning Books ---")
library.return_book(301, 101)
library.return_book(302, 101)


print("\n--- Display After Returns ---")
library.display_member_books(301)
library.display_available_books()


print("\n--- Error Handling Tests ---")
library.borrow_book(999, 101)
library.borrow_book(301, 999)
library.return_book(999, 101)
library.display_member_books(999)
