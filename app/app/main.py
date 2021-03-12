# main.py
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from app.db.database import SessionLocal
from app import crud, models, schemas

app = FastAPI()

#: Configure CORS
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    print(type(db_user))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/words/", response_model=List[schemas.Word])
def read_words(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    words = crud.get_words(db, skip=skip, limit=limit)
    return words


@app.post("/words/", response_model=schemas.Word)
def create_word(word: schemas.WordCreate, db: Session = Depends(get_db)):
    db_word = crud.get_word(db, name=word.name)
    if db_word:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_word(db=db, word=word)


@app.post("/means/", response_model=schemas.Mean)
def create_mean(word: schemas.WordCreate, mean: schemas.MeanCreate, db: Session = Depends(get_db)):
    db_word = crud.get_word(db, name=word.name)
    if db_word is None:
        crud.create_word(db=db, word=word)
    return crud.create_mean(db, mean=mean, owner_word=word.name)
