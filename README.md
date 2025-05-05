# Library-Management-System
This project is a Tkinter-based GUI application for managing library operations efficiently. It allows librarians to add, view, update, issue, return, and delete books with an intuitive interface. The system uses SQLite for database storage, ensuring data persistence.
(This is a group project done in my graduation as a major project)

Key Features
Book Management

Add Books: Store book details such as Book ID, Title, and Author.

View Books: Display all available books in a structured table format with sorting capabilities.

Update Books: Modify existing book records when needed.

Delete Books: Remove books individually or clear the entire database.

Book Issuance & Returns

Issue Books: Record which student has borrowed a book, along with their name, phone, and address.

Return Books: Track when books are returned with automatic timestamp updates.

View Issued Books: Check all issued books with details like student name, issue date, and return status.

Database Integration

Uses SQLite for storing book and student records.

Persistent storage ensures data remains intact between sessions.

User-Friendly Interface

Built with Tkinter for a clean and responsive GUI.

Treeview widgets for displaying data in tables.

OS module for dynamic file path handling, making the application portable.

Technical Stack
Frontend: Tkinter (Python GUI)

Backend: SQLite (Database)

Additional Libraries:

Pillow (PIL) for image handling (logo and background)

datetime for tracking issue and return dates
