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

---

## Technologies Used
- **Python** – Core programming language
- **Django** – Web framework for backend development
- **SQLite** – Lightweight relational database
- **HTML/CSS** *(if frontend used)*
- **Git & GitHub** – Version control and project hosting

---

## CRUD Operations
### Create
Add a new student record with name, age, and course details.

### Read
Display all student records stored in the database.

### Update
Modify existing student details whenever required.

### Delete
Remove student records from the database.

---

## Project Structure
```bash
Crud_Operation/
|── .env
│── studentapp/
|── |── migration
|── |── _init_.py
|── |── admin.py
|── |── apps.py
|── |── models.py
|── |── tests.py
|── |── urls.py
|── |── views.py
│── studentproject/
│   │── _init_.py/
│   │── asgi.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│ ── db.sqllite3
│ ── manage.py
```

---

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
Developed by **Dharshan L**

---

## OUTPUT Post method  using Data Stored in Postman

## Create

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f7f2cec4-5899-40cc-ab34-a4d6994dc0eb" />

---

## Read
<img width="1920" height="1080" alt="Screenshot 2026-05-23 105641" src="https://github.com/user-attachments/assets/e44fb915-740f-4366-af77-82349448e5fd" />


---

## Update
<img width="1920" height="1080" alt="Screenshot 2026-05-23 105827" src="https://github.com/user-attachments/assets/3e73e83d-451c-4c6d-b9d2-42d7b095632b" />


---

## Delete
<img width="1920" height="1080" alt="Screenshot 2026-05-23 105854" src="https://github.com/user-attachments/assets/b0938ce8-28e1-402c-9b1a-002690113fc1" />

---




