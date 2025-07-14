# 📦 WebAPI - How to Run

This document explains how to set up, run, and test the backend service.

---

## ✅ 1️⃣ Install dependencies

Make sure you have **Python 3.10+** installed.

Install all required Python packages with:

```bash
pip install -r requirements.txt
```

---

## ✅ 2️⃣ Run the server locally

To start the FastAPI server in development mode (with auto-reload):

```bash
uvicorn api.app:app --reload
```

The server will be available at:

- http://127.0.0.1:8000/

---

## ✅ 3️⃣ Explore the API Docs

After starting the server, visit:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## ✅ 4️⃣ Run tests

To run the complete test suite with pytest:

```bash
python -m pytest
```

For HTML reports (optional):

```bash
pytest --html=report.html
```

---

## ✅ 5️⃣ Notes

- This project does **not** use a database. All data is read from local JSON files.
- Security is implemented with JWT authentication.
- Tests cover at least 80% of the codebase, including:
  - Login success/failure
  - Access with/without tokens
  - 404 for non-existent products
  - Token expiration and invalid token handling

---
