
# 📦 Inventory Management API

A clean and production-style CRUD Inventory System built with FastAPI + SQLModel + SQLite, designed to demonstrate backend development, REST API design, and SQL analytics capabilities.

This project is perfect for showcasing skills in Python, SQL, backend engineering, testing, and API development—ideal for Software Developer and Backend Engineer roles.

## 🚀 Features

### 🔹 Core Functionality

- Create, Read, Update, Delete (CRUD) inventory items
- Pagination & keyword search
- Auto-generated documentation (Swagger / ReDoc)
- SQLite database integration with SQLModel
- Timestamped records (created_at, updated_at)
- Background DB initialization on startup

### 🔹 Developer Features

- Clean project structure
- API-first design
- Unit tests with PyTest
- Easy to run and extend
- Beginner-friendly, but production-ready patterns

  
## 📸 Screenshots 

<img width="1220" height="780" alt="Screenshot 2025-12-13 025226" src="https://github.com/user-attachments/assets/ce33b32d-7ba5-46aa-ab5e-6cfa34883324" />7
<img width="1220" height="780" alt="Screenshot 2025-12-13 025246" src="https://github.com/user-attachments/assets/ac7b36a8-9daf-4ae6-9c1c-39dd945396be" />

<img width="1118" height="805" alt="Screenshot 2025-12-13 025712" src="https://github.com/user-attachments/assets/eb35ec96-2a66-4594-9bc3-b78d5337d857" />


## 🗂 Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python |
| Framework | FastAPI |
| ORM | SQLModel (SQLite backend) |
| Testing | PyTest, TestClient |
| Server | Uvicorn |
| Database | SQLite (file-based, no setup needed) |

## 📁 Project Structure
```
inventory-system/
│── main.py
│── models.py
│── database.py
│── requirements.txt
│── README.md
│── tests/
│     └── test_items.py
│── .gitignore
```

## ▶ Running the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the server
```bash
uvicorn main:app --reload
```

### 3. Open API documentation

- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

## 🔥 API Endpoints

### Root

**GET /** - Returns a welcome message + endpoint info.

### Inventory

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /items | Create a new item |
| GET | /items | List all items (pagination + search) |
| GET | /items/{item_id} | Get item by ID |
| PUT | /items/{item_id} | Update item |
| DELETE | /items/{item_id} | Delete item |

## 🧪 Testing

Run all tests:
```bash
pytest
```

Includes:
- Test for creating new items
- Test for listing items

## 🗄 Database Schema

**Item table:**

| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Auto-generated |
| name | Text | Item name |
| sku | Text | Unique stock code |
| qty | Integer | Quantity available |
| price | Float | Unit price |
| created_at | Timestamp | Auto-set on create |
| updated_at | Timestamp | Auto-updated on update |

## 📚 Example JSON Body

### ✔ Create Item (POST /items)
```json
{
  "name": "Tablet",
  "sku": "TB-001",
  "qty": 15,
  "price": 40000
}
```

## 📊 SQL Analytics Queries (Advanced)

Here are powerful SQL queries you can run in DB Browser for SQLite.

### 1. List all items
```sql
SELECT * FROM item;
```

### 2. Total number of items
```sql
SELECT COUNT(*) AS total_items FROM item;
```

### 3. Total inventory value
```sql
SELECT SUM(qty * price) AS total_value FROM item;
```

### 4. Low stock items
```sql
SELECT name, qty FROM item WHERE qty < 5;
```

### 5. Top 5 most expensive items
```sql
SELECT name, price FROM item ORDER BY price DESC LIMIT 5;
```

### 6. Items priced between 500 and 2000
```sql
SELECT * FROM item WHERE price BETWEEN 500 AND 2000;
```

### 7. Search items
```sql
SELECT * FROM item WHERE name LIKE '%lap%';
```

### 8. Bucketed price ranges
```sql
SELECT
  CASE
    WHEN price < 500 THEN 'Under 500'
    WHEN price BETWEEN 500 AND 2000 THEN '500–2000'
    WHEN price BETWEEN 2001 AND 5000 THEN '2001–5000'
    ELSE 'Above 5000'
  END AS price_range,
  COUNT(*) AS total
FROM item
GROUP BY price_range;
```

### 9. Average price
```sql
SELECT AVG(price) FROM item;
```

### 10. Latest items
```sql
SELECT * FROM item ORDER BY created_at DESC;
```

## 🧱 Sample Seed Data (Insert Queries)

You can populate your database with this sample data:
```sql
INSERT INTO item (name, sku, qty, price, created_at, updated_at)
VALUES ("Laptop", "LP-001", 10, 55000, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
```


## 🧑‍💻 Author

**Varun Rathore**  
📍 Ujjain, MP  
🔗 GitHub: https://github.com/VarunRathore137  
🔗 LinkedIn: https://www.linkedin.com/in/varun-rathore137

## ⭐ If you like this project

Give the repo a ⭐ on GitHub — it helps!

