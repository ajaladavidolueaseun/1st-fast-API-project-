from fastapi import FastAPI
from database import engine, Base
from routers import lecturers

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lecturers API with PostgreSQL")

app.include_router(lecturers.router)

@app.get("/")
def root():
    return {"message": "API is running successfully"}
