from library_oop import Library

print("=== TESTING CLASS: Library ===")

library = Library()
print("\n--- Adding Books ---")
library.add_book(101, "Sword Art Online: Aincrad", "Reki Kawahara", 4)
library.add_book(102, "Demon Slayer: Final Selection", "Koyoharu Gotouge", 2)
library.add_book(103, "Your Name: Another Side", "Makoto Shinkai", 1)

print("\n--- Adding Members ---")
library.add_member(301, "Kirito Kirigaya", "kirito@aincrad.jp")
library.add_member(302, "Nezuko Kamado", "nezuko@slayer.jp")

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