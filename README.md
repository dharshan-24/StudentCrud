# Student Management System - CRUD Application

A simple and efficient Student Management System built using Django that performs full CRUD (Create, Read, Update, Delete) operations for managing student records.

## Project Overview
This project is designed to manage student information such as:
- Student Name
- Age
- Course

It demonstrates the implementation of core CRUD functionality using Django framework with SQLite database integration.

## Features
✅ Add new student records  
✅ View all student details  
✅ Update existing student information  
✅ Delete student records  
✅ User-friendly interface  
✅ Database storage using SQLite  
✅ Clean project structure following Django MVC architecture  

## Technologies Used
- **Python** – Core programming language
- **Django** – Web framework for backend development
- **SQLite** – Lightweight relational database
- **HTML/CSS** *(if frontend used)*
- **Git & GitHub** – Version control and project hosting

## CRUD Operations
### Create
Add a new student record with name, age, and course details.

### Read
Display all student records stored in the database.

### Update
Modify existing student details whenever required.

### Delete
Remove student records from the database.

## Project Structure
```bash
student_crud/
│── manage.py
│── student_crud/
│── students/
│   │── migrations/
│   │── models.py
│   │── views.py
│   │── urls.py
│   │── templates/
│   │── admin.py
│   │── forms.py
```

## Installation Steps

### 1. Clone Repository
```bash
git clone https://github.com/your-username/student-crud.git
```

### 2. Move to Project Folder
```bash
cd student-crud
```

### 3. Create Virtual Environment
```bash
python -m venv venv
```

### 4. Activate Virtual Environment
Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install django
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start Development Server
```bash
python manage.py runserver
```

### 8. Open in Browser
```bash
http://127.0.0.1:8000/
```

## Learning Objectives
This project helps in understanding:
- Django project structure
- Models, Views, Templates
- Database operations with SQLite
- Form handling
- CRUD implementation
- GitHub project deployment basics

## Future Improvements
- Search student records
- Pagination
- Authentication/Login system
- REST API integration
- Bootstrap UI enhancement

## Author
Developed by **Your Name**
