# 🚀 Portfolio API - FastAPI CRUD

A professional REST API project built with Python and FastAPI, focused on learning backend architecture, CRUD operations, and API organization patterns.

This project is part of a progressive backend roadmap:

* ✅ Version 1 — In-Memory Storage
* 🔜 Version 2 — SQLite Database
* 🔜 Version 3 — PostgreSQL + ORM

---

# 📌 Features

* Create Projects
* List Projects
* Update Projects
* Delete Projects
* HTTP Exception Handling
* Organized FastAPI Structure
* Temporary In-Memory Database

---

# 🛠️ Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic

---

# 📂 Project Structure

```bash
portfolio-api-python/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │    └── projects.py
│   ├── database/
│   │    └── memory_db.py
│
├── requirements.txt
└── README.md
```

---

# ▶️ Running the Project

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/portfolio-api-python.git
```

---

## 2. Enter the project folder

```bash
cd portfolio-api-python
```

---

## 3. Create virtual environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the server

```bash
uvicorn app.main:app --reload
```

---

# 📚 API Documentation

After running the server:

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

ReDoc:

```bash
http://127.0.0.1:8000/redoc
```

---

# 📌 Available Endpoints

| Method | Endpoint       | Description          |
| ------ | -------------- | -------------------- |
| GET    | /projects      | List all projects    |
| POST   | /projects      | Create a new project |
| PUT    | /projects/{id} | Update a project     |
| DELETE | /projects/{id} | Delete a project     |

---

# 🧠 Example JSON

```json
{
  "title": "Portfolio API",
  "description": "FastAPI CRUD project"
}
```

---

# ⚠️ Current Limitation

This version uses temporary in-memory storage.

Data is reset every time the server restarts.

---

# 🚀 Future Improvements

* SQLite integration
* PostgreSQL integration
* SQLAlchemy ORM
* Authentication with JWT
* Docker support
* Automated tests
* Deploy on Render/Railway

---

# 👨‍💻 Author

Developed by Alisson Labs.

Focused on backend development, APIs, automation, and scalable systems.

---
