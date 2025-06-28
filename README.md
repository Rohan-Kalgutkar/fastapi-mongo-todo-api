# 📝 FastAPI Todo App with MongoDB

A simple Todo application built with FastAPI and MongoDB.

## 🚀 Features

- Create, read, update, delete todos
- MongoDB Atlas integration
- Pydantic validation
- Auto-generated Swagger UI
- Environment variables for security

## 📁 Folder Structure

- `main.py` — App entry point
- `route.py` — API routes
- `models/todos.py` — Pydantic model
- `schemas.py` — Mongo object serialization
- `database.py` — MongoDB setup

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-mongo-todo.git
   cd fastapi-mongo-todo
   ```

2. Create a `.env` file in the root directory and add:
   ```env
   MONGO_URI=your_mongodb_connection_string
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8000/docs
   ```

## 📦 Tech Stack

- FastAPI
- Pydantic
- MongoDB (via PyMongo)
- Swagger UI

## ✅ TODO
- [ ] Add user authentication
- [ ] Pagination for todos
- [ ] Frontend (React/Next.js)

---

Made with ❤️ using FastAPI
