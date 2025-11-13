from library_oop import Book


print('\n=== TESTING: Book class ===\n')

book1 = Book(1, 'Python Crash Course', 'Eric Matthes', 3)


print('Title =>', book1.title)
print('Author =>', book1.author)
print('Total copies =>', book1.total_copies)
print('Available =>', book1.available_copies)

print('\n-- Borrowing a few copies --')
book1.borrow_copy()
book1.borrow_copy()
print('Now available:', book1.available_copies)

print('\n-- Borrowing again (may fail) --')
ok = book1.borrow_copy()
print('Borrow successful?', ok)
print('Copies left:', book1.available_copies)

print('\n-- Returning one copy --')
book1.return_copy()
print('Copies available after return =', book1.available_copies)
