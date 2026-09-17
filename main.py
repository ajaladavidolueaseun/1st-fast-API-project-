from fastapi import FastAPI, HTTPException
from data import lecturers_data

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Lecturer Courses API"}


@app.get("/lecturers")
def get_all_lecturers():
    return lecturers_data


@app.get("/lecturers/{name}")
def get_lecturer_courses(name: str):
    if name not in lecturers_data:
        raise HTTPException(status_code=404, detail="Lecturer not found")
    return {"lecturer": name, "courses": lecturers_data[name]}