from fastapi import APIRouter, HTTPException, Form
from api.security import create_jwt_token

router = APIRouter()

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "password":
        token = create_jwt_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")