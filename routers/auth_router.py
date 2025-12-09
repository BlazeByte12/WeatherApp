import sqlite3
from fastapi import APIRouter, HTTPException, Depends
from database import get_db_connection
from models.user import UserCreate, UserLogin
from auth.generate_key import generate_api_key

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )
        conn.commit()
        return {"message": "User registered successfully!"}

    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Username already exists.")

@router.post("/login")
def login(user: UserLogin):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, password FROM users WHERE username = ?",
        (user.username,)
    )
    result = cursor.fetchone()

    if not result or result["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    api_key = generate_api_key()

    cursor.execute("UPDATE users SET api_key = ? WHERE id = ?", (api_key, result["id"]))
    conn.commit()
    conn.close()

    return {"api_key": api_key}
