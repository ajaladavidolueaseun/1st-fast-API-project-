from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lecturers API with PostgreSQL")

@app.post("/lecturers/", response_model=schemas.LecturerResponse, status_code=status.HTTP_201_CREATED)
def create_lecturer(lecturer: schemas.LecturerCreate, db: Session = Depends(get_db)):
    db_lecturer = models.Lecturer(**lecturer.model_dump())
    db.add(db_lecturer)
    db.commit()
    db.refresh(db_lecturer)
    return db_lecturer

@app.get("/lecturers/", response_model=list[schemas.LecturerResponse])
def get_lecturers(db: Session = Depends(get_db)):
    return db.query(models.Lecturer).all()