# 🎨 WebAPI - Design Document

---

## ✅ Objective

Implement a RESTful API to serve product details for a MercadoLibre-style Item Detail Page, with local JSON storage and JWT-based authentication.

---

## ✅ Stack & Architecture

- **Backend:** Python 3.10+ with FastAPI
- **Persistence:** Local JSON file
- **Security:** JWT (PyJWT)
- **Tests:** pytest
- **Architecture:** Hexagonal-inspired layout
  - api/ for routes and security
  - infrastructure/ for repositories
  - tests/ for test suite

---

## ✅ Why FastAPI?

- Rapid development and clean syntax.
- Automatic OpenAPI docs generation.
- First-class support for JSON and form parsing.
- Built-in dependency injection.

---

## ✅ Main Endpoints

### /login

- **POST** accepting username/password as form data.
- Returns a JWT on success.
- Hard-coded user ("admin" / "password").

---

### /items/{product_id}

- **GET** with Authorization: Bearer <token>.
- Reads product details from a local JSON file.
- Returns 404 if not found.
- Returns product data designed to match MercadoLibre-like detail page.

---

## ✅ Data Model

Product details include:

- Images (gallery)
- Title, description
- Price, discount, installments
- Variants/colors
- Stock
- Specifications
- Related products
- Seller info
- Payment methods

---

## ✅ Error Handling

- 401 Unauthorized for missing/invalid tokens.
- 403 Forbidden for unauthorized access.
- 404 Not Found for missing products.
- Token expiration handling.

---

## ✅ Challenges & How They Were Solved

✅ **Form Parsing in /login**
- Used FastAPI's Form() for proper parsing.

✅ **JWT Integration**
- Used PyJWT.
- Implemented token creation and verification with expiration.
- Managed HS256 algorithm and secret securely.

✅ **Local Data Storage**
- No real DB: Reads from a local JSON file.
- Ensured data structure is flexible for adding features.

✅ **Testing Coverage**
- Used pytest and httpx for TestClient.
- Covered success and failure cases.
- Tested auth errors, 404s, token expiration.

---

## ✅ Notes

- The API is stateless.
- Easy to swap JSON for a real DB later.
- Designed for clarity and ease of maintenance.

---
