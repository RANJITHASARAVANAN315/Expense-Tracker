# Expense Tracker Web Application

A simple and clean Expense Tracker built using **Flask, HTML, CSS, JavaScript, and MySQL**.
It allows users to:

✔ Add new expenses
✔ View all expenses
✔ Calculate total spending
✔ Store data in MySQL database
✔ Use a modern UI with gradients and clean layout

---

## 🚀 Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python Flask
* **Database:** MySQL
* **IDE Used:** VS Code

---

## 📂 Project Structure

```
Expense-Tracker/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── add_expense.html
│   ├── view_expenses.html
│   └── total_expense.html
│
└── static/
    └── style.css
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### 2️⃣ Create Virtual Environment (Optional)

```
python -m venv venv
```

Activate it:

* Windows:

```
venv\Scripts\activate
```

* Linux / Mac:

```
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Configure MySQL Database

Open MySQL and run:

```sql
CREATE DATABASE expenses_db;

USE expenses_db;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(255),
    amount FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5️⃣ Update Database Credentials

Inside `app.py`, update:

```python
host="YOUR_HOST",
user="YOUR_USERNAME",
password="YOUR_PASSWORD",
database="expenses_db"
```

### 6️⃣ Run the App

```
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## ✨ Features

* Responsive UI with modern styling
* Add and store expenses easily
* View expenses in tabular format
* Get total spending instantly
* Fully working backend

---

## 🤝 Contributing

Pull requests are welcome!
If you want to improve UI, add user login, graphs, or API support, feel free to contribute.

---

## 📄 License

This project is open-source and available under the MIT License.

---

⭐ If you like this project, don’t forget to star the repository!
