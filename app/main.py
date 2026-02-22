from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from . import models, database, schemas, crud
from .recommendation import generate_meal_plan
import shutil
from .image_analysis import predict_food, get_nutrition


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.post("/meals", response_model=schemas.MealResponse)
def create_meal(meal: schemas.MealCreate, db: Session = Depends(get_db)):
    return crud.create_meal(db, meal)


@app.get("/meals", response_model=list[schemas.MealResponse])
def get_meals(db: Session = Depends(get_db)):
    return crud.get_all_meals(db)


@app.get("/recommend/{user_id}")
def recommend(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    meals = crud.get_all_meals(db)

    result = generate_meal_plan(user, meals)

    return result


@app.post("/analyze-food")
async def analyze_food(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    label, confidence = predict_food(file_path)
    nutrition = get_nutrition(label)

    return {
        "food_name": label,
        "confidence": confidence,
        "nutrition": nutrition
    }
