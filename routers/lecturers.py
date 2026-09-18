from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(
    prefix="/lecturers",
    tags=["Lecturers"]
)

@router.post("/", response_model=schemas.LecturerResponse, status_code=status.HTTP_201_CREATED)
def create_lecturer(lecturer: schemas.LecturerCreate, db: Session = Depends(get_db)):
    db_lecturer = models.Lecturer(**lecturer.model_dump())
    db.add(db_lecturer)
    db.commit()
    db.refresh(db_lecturer)
    return db_lecturer

@router.get("/", response_model=list[schemas.LecturerResponse])
def get_lecturers(db: Session = Depends(get_db)):
    return db.query(models.Lecturer).all()

@router.get("/{lecturer_id}", response_model=schemas.LecturerResponse)
def get_lecturer(lecturer_id: int, db: Session = Depends(get_db)):
    lecturer = db.query(models.Lecturer).filter(models.Lecturer.id == lecturer_id).first()
    if not lecturer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lecturer not found")
    return lecturer

@router.put("/{lecturer_id}", response_model=schemas.LecturerResponse)
def update_lecturer(lecturer_id: int, updated_data: schemas.LecturerCreate, db: Session = Depends(get_db)):
    query = db.query(models.Lecturer).filter(models.Lecturer.id == lecturer_id)
    lecturer = query.first()
    if not lecturer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lecturer not found")
    
    query.update(updated_data.model_dump(), synchronize_session=False)
    db.commit()
    return query.first()

@router.delete("/{lecturer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lecturer(lecturer_id: int, db: Session = Depends(get_db)):
    query = db.query(models.Lecturer).filter(models.Lecturer.id == lecturer_id)
    lecturer = query.first()
    if not lecturer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lecturer not found")
    
    query.delete(synchronize_session=False)
    db.commit()
    return None
