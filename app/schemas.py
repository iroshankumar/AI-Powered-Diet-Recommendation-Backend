from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0)
    height: int = Field(..., gt=0)
    weight: int = Field(..., gt=0)
    activity_level: str
    dietary_preference: str
    health_goal: str
    allergies: str | None = None


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True



class MealCreate(BaseModel):
    name: str
    calories: float
    protein: float
    carbs: float
    fat: float
    diet_type: str


class MealResponse(MealCreate):
    id: int

    class Config:
        from_attributes = True