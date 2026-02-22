# AI-Powered Diet Recommendation Backend

A backend service that generates personalized meal recommendations based on user profile data such as age, weight, activity level, and health goals.

This project also includes image-based food analysis using a pretrained deep learning model (MobileNetV2).

---

## Features

- User Profile Management API
- Nutrition Dataset Management
- Rule-Based Meal Recommendation Engine
- Calorie Calculation using BMR Formula
- Goal-Based Calorie Adjustment
- Image-Based Food Identification (TensorFlow)
- MySQL Database Integration
- Interactive API Documentation (Swagger)

---

## Architecture Overview

Client  
⬇  
FastAPI Routes  
⬇  
Pydantic Schemas (Validation Layer)  
⬇  
CRUD Layer  
⬇  
SQLAlchemy Models  
⬇  
MySQL Database  

Additional Modules:
- Recommendation Engine (Business Logic)
- Image Analysis Module (Deep Learning)

---

##  Tech Stack

- **Backend:** FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **AI Model:** TensorFlow (MobileNetV2)
- **Server:** Uvicorn

---

##  Recommendation Logic

1. Calculate Basal Metabolic Rate (Mifflin-St Jeor approximation)
2. Adjust calories using activity multiplier
3. Modify calories based on health goal:
   - Weight Loss → Calorie Deficit
   - Muscle Gain → Calorie Surplus
   - Maintenance → No Change
4. Filter meals based on dietary preference
5. Select meals using a calorie-based greedy approach

---

## Image-Based Food Analysis

- Accepts food image upload
- Uses pretrained MobileNetV2 (ImageNet)
- Predicts food category
- Maps predicted food to approximate nutrition values
- Returns:
  - Food Name
  - Estimated Calories
  - Protein
  - Carbohydrates
  - Fat

---

## 📦 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/iroshankumar/AI-Powered-Diet-Recommendation-Backend/tree/main
cd diet-ai-backend

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate


3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the project root:

DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=diet_ai

5️⃣ Create Database

Login to MySQL and run:

CREATE DATABASE diet_ai;

6️⃣ Run the Application
uvicorn app.main:app --reload


## API Documentation

Swagger UI available at:

http://127.0.0.1:8000/docs

---

API Endpoints
➤ Create User

POST /users

➤ Add Meal

POST /meals

➤ Get Recommendation

GET /recommend/{user_id}

➤ Analyze Food Image

POST /analyze-food

Future Improvements

Add gender field for more accurate BMR calculation

Optimize meal selection using linear programming

Add macro-balanced meal distribution

Replace rule-based logic with ML personalization

Docker containerization

Add authentication system

## Author

Roshan Kumar
AI/ML Engineer