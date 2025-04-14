# 📚 BookEase

BookEase is a Django REST API-based application that allows users to manage books, user accounts, and personal reading lists. The frontend and backend are maintained in separate repositories.

---

## 🔗 Live Project Links

- **Backend**: [BookEase Backend (Live API)](https://bookease-backend.onrender.com)

---

## ⚙️ Features

### ✅ User Management
- User Registration
- JWT Login & Token Refresh
- User Profile View & Update

### ✅ Book Management
- Add, Remove, View All Books
- Books include: Title, Author(s), Genre, Publication Date, Description

### ✅ Reading List
- Create & Manage Personal Reading Lists
- Organize books in preferred order (Drag and Drop)

---

## 🧪 API Endpoints

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/registration/` | POST | Register a new user |
| `/login/` | POST | Obtain JWT access/refresh token |
| `/token/refresh/` | POST | Refresh JWT token |
| `/get_user_details/` | GET | Retrieve current user's profile |
| `/update_user/` | PATCH | Update user profile |
| `/bookmanagement/` | POST/GET/DELETE/PUT | Manage books |
| `/readinglist_management/` | POST/GET/DELETE/PUT| Manage reading list |

> All endpoints follow RESTful design.

---

## 🛡️ Authentication

This project uses **JWT (JSON Web Token)** for secure authentication.

---

## 🔧 Tech Stack

- Backend: **Django**, **Django REST Framework**
- Database: **PostgreSQL**
- Authentication: **JWT (via SimpleJWT)**
- Frontend: **React js , Redux toolkit**

---

Edit

---

## 🧾 Environment Setup

### 1. Clone the Repositories

    git clone https://github.com/umarulshahin/BookEase_Backend.git
2. Backend Setup

       python -m venv env
3. Activate Environment

       env\Scripts\activate
4. Set up requirment packages

       pip install -r requirements.txt


4. Create .env file
In your backend root: After creating .env add

        SECRET_KEY=your_secret_key_here
        DATABASE_URL=postgres://username:password@host:port/dbname
Replace with your actual database credentials.

5. Apply Migrations

       python manage.py makemigrations
       python manage.py migrate

6. Run Server

       python manage.py runserver
