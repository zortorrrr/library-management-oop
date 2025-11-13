# Library Management System (Object-Oriented Version)

## Project Overview
This project is a refactored version of a procedural library management program rewritten using Object-Oriented Programming (OOP) principles.  
The system manages books, members, borrowing, and returning operations.  
The goal of this assignment is to demonstrate:
- Class design
- Object interactions
- Encapsulation
- Improved code organization compared to the procedural version

This OOP implementation includes three main classes: **Book**, **Member**, and **Library**.  
A comprehensive test file (`test_oop.py`) is also provided to validate all core and edge-case functionality.

---

## Project Structure

library-management-oop/
│
├── README.md
│
├── procedural_version/
│ ├── library_procedural.py
│ └── test_procedural.py
│
├── oop_solution/
│ ├── library_oop.py # OOP implementation (Book, Member, Library)
│ └── test_oop.py # Comprehensive test suite


---

## Design Overview

### 1. **Book Class**
Represents a book in the library.

**Attributes**
- `code` — unique ID of the book  
- `name` — book title  
- `writer` — author of the book  
- `copies_total` — total number of copies  
- `copies_left` — available copies remaining  

**Key Methods**
- `borrow_copy()`  
  Decreases `copies_left` if the book is available.
- `return_copy()`  
  Increases `copies_left` when a copy is returned.

---

### 2. **Member Class**
Represents a library user.

**Attributes**
- `ident` — unique member ID  
- `nickname` — member's displayed name  
- `contact` — email or contact information  
- `items_on_loan` — list of borrowed `Book` objects  

**Key Methods**
- `borrow_book(book)`  
  Allows member to borrow a book (limit: 3 books).
- `return_book(book)`  
  Handles returning a book, updating availability.

---

### 3. **Library Class**
Coordinates and manages books and members in the system.

**Attributes**
- `books` — list of `Book` objects  
- `members` — list of `Member` objects  
- `loan_records` — internal record of borrowing transactions  

**Key Methods**
- `add_book(code, name, writer, copies_total)`
- `add_member(ident, nickname, contact)`
- `find_book(book_code)`
- `find_member(member_code)`
- `borrow_book(member_id, book_id)`
- `return_book(member_id, book_id)`
- `display_available_books()`
- `display_member_books(member_id)`

---

## Testing

All testing is done using `test_oop.py`, which covers both basic operations and edge cases.

### ✔ Basic Operations
- **Adding books and members**  
  Ensures system can register new books and users.
- **Borrowing books**  
  Updates member’s borrowed list and book availability.
- **Returning books**  
  Restores book availability and updates records.
- **Displaying information**  
  Shows available books and books borrowed per member.

### ✔ Edge Cases
- **Borrowing unavailable books**  
  System correctly prevents borrowing when no copies remain.
- **Exceeding borrowing limit**  
  Members cannot borrow more than three books.
- **Returning books not borrowed**  
  Handles invalid return attempts safely.
- **Non-existent books/members**  
  Validates incorrect IDs during borrow/return operations.

---

## How to Run the Test Code

To run the test suite for the OOP version of the library system, follow these steps:

1. Open a terminal and navigate to the `oop_solution/` directory:

```bash
cd oop_solution
```

2. Execute the test file using Python:

```bash
python3 test_oop.py
```

3. You should see output for:
- Adding books and members  
- Borrowing and returning operations  
- Displaying available books  
- Edge-case handling  
- Final library status summary  

This confirms that all classes and methods in the OOP implementation are functioning correctly.

