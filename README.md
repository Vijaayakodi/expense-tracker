# 💰 Expense Tracker

A modern **Full-Stack Expense Tracker** built with **Flask, MySQL, HTML, CSS, and JavaScript**. This application allows users to manage their income and expenses through a clean and responsive interface while storing data securely in a MySQL database.

---

## 📌 Features

- ✅ Add new transactions
- ✅ View all transactions
- ✅ Delete transactions
- ✅ Live balance summary
- ✅ Income & Expense tracking
- ✅ REST API using Flask
- ✅ MySQL database integration
- ✅ Responsive user interface
- ✅ Fetch API for frontend-backend communication

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript (ES6)
- Fetch API

### Backend
- Python
- Flask
- Flask-CORS

### Database
- MySQL

### Tools
- VS Code
- Git
- GitHub
- Postman

---

## 📂 Project Structure

```
expense-tracker/
│
├── backend/
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── app.py
│   ├── routes.py
│   ├── models.py
│   ├── database.py
│   ├── config.py
│   └── test_connection.py
│
├── database/
│   └── expense_tracker.sql
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Vijaayakodi/expense-tracker.git
```

### 2. Navigate to the project

```bash
cd expense-tracker
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file.

Example:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=expense_tracker
```

---

### 6. Import Database

Import

```
database/expense_tracker.sql
```

into MySQL.

---

### 7. Run the application

```bash
cd backend
python app.py
```

---

### 8. Open in browser

```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### Get All Transactions

```
GET /transactions
```

---

### Add Transaction

```
POST /transactions
```

Example JSON

```json
{
    "title": "Lunch",
    "amount": 250,
    "category": "Food",
    "type": "Expense",
    "transaction_date": "2026-07-02",
    "notes": "Lunch with friends"
}
```

---

### Delete Transaction

```
DELETE /transactions/<id>
```

---

### Financial Summary

```
GET /summary
```

Returns

- Total Income
- Total Expense
- Current Balance

---

## 📸 Screenshots

Coming Soon...

---

## 🎯 Future Enhancements

- ✏️ Edit Transactions
- 🔍 Search Transactions
- 📅 Date Filter
- 📂 Category Filter
- 📊 Expense Charts
- 📈 Monthly Analytics
- 📄 Export to PDF
- 📥 Export to Excel
- 👤 User Authentication
- 🌙 Dark Mode
- ☁️ Cloud Deployment

---

## 🎓 What I Learned

Through this project I learned:

- Flask REST API Development
- CRUD Operations
- MySQL Database Integration
- JavaScript Fetch API
- Frontend & Backend Communication
- Git & GitHub Version Control
- API Testing using Postman
- Environment Variables
- Full-Stack Project Structure

---

## 👨‍💻 Author

**Vijaayakodi G L**

GitHub:
https://github.com/Vijaayakodi

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
