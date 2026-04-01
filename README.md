# 🛠️ Campus Classroom Tracker

A full-stack web application designed for university residents and faculty to report and track maintenance issues in classrooms. This project features a **React** frontend, a **FastAPI** backend, and a **PostgreSQL** database.

## 🚀 Features
* **Relational Database:** Stores Users, Rooms, and Tickets with strict data integrity.
* **Interactive API:** Built-in Swagger UI for testing endpoints.
* **Live Dashboard:** React-based frontend that pulls real-time ticket data from the database.
* **Auto-Diagnosis Ready:** Includes PostgreSQL extensions for advanced search and diagnosis.

## 🏗️ Project Architecture
* **Frontend:** React (Vite)
* **Backend:** Python (FastAPI + SQLAlchemy)
* **Database:** PostgreSQL 18

---

## ⚙️ Setup & Installation

### 1. Database Setup
1. Install and run **Postgres.app** (PostgreSQL 18).
2. Set the server to run on port `5433`.
3. Open **pgAdmin 4** and connect to your local server.
4. Create a new database named `classroom_tracker`.
5. In the **Definition** tab, set **Locale Provider** to `icu`.
6. Open the **Query Tool** and run the SQL schema to generate the tables.

### 2. Backend Setup (FastAPI)
```bash
# Navigate to the project root
cd CampusTracker

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

### 3. Frontend Setup (React)
```bash
# Navigate to the frontend folder
cd frontend

# Install dependencies
npm install
```

---

## 🏃 How to Start the Project

To run the application, open two separate terminal tabs in VS Code:

#### Tab 1: Start the Backend
```bash
# Ensure venv is active
source venv/bin/activate
uvicorn main:app --reload
```
API will be live at: `http://127.0.0.1:8000/docs`

#### Tab 2: Start the Frontend
```bash
cd frontend
npm run dev
```
Web app will be live at: `http://localhost:5173`

---

## 📝 Future Roadmap
* [ ] Implement a "Report Issue" form on the frontend.
* [ ] Add Technician specialized views to update ticket progress.
* [ ] Add user authentication for students and faculty.

---

Once you hit **Commit changes** on GitHub, your project will look professional and ready for your next session. Great work today, Adi!
