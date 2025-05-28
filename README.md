Student Management System (CRUD) with Django Generic Class-Based Views
This project is a Student Management System built using Django and Generic Class-Based Views (GCBV). It provides a complete CRUD (Create, Read, Update, Delete) interface for managing student records efficiently.

Features
✅ Add New Students – Collects student details (name, address, roll number, grade, email, gender, date of birth, and profile picture).
✅ View Student List – Displays all students in a tabular/list format.
✅ View Student Details – Shows detailed information about a specific student.
✅ Update Student Records – Allows modification of existing student data.
✅ Delete Students – Removes student entries from the database.
✅ Success Messages – Provides feedback upon successful operations (e.g., "1 Student(s) added successfully!").

Technologies Used
Backend: Django (Python)

Frontend: HTML, Bootstrap (for styling)

Database: SQLite (default Django DB)

Django Features Used:

Generic Class-Based Views (CreateView, ListView, DetailView, UpdateView, DeleteView)

Success messages using SuccessMessageMixin

Model forms for data handling

Setup & Installation
Clone the Repository


Future Improvements
Search & Filtering – Allow searching students by name, roll, or grade.

Pagination – Split student lists into multiple pages.

User Authentication – Restrict access to authorized users.

Export Data – Export student records to CSV/Excel.

Contributing
Feel free to fork this project and submit pull requests. For major changes, open an issue first.
