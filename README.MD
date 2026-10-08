# Insurance Premium Predictor

A REST API built with FastAPI that predicts a user's insurance premium category (low, medium or high) using a Random Forest classifier.

## How it works
Users submit their age, height, weight, annual income (LPA), smoker status, occupation and city. The API validates the input with Pydantic and derives extra features:

- BMI from height and weight
- Lifestyle risk from smoker status and BMI
- Age group (young, adult, middle aged, senior)
- City tier (Tier 1, 2 or 3), covering most major Indian cities

These features are passed to the trained model, which returns the predicted premium category.

## Tech stack
Python, FastAPI, Pydantic, scikit-learn (Random Forest), pandas, Uvicorn

## Run locally
pip install fastapi uvicorn pandas scikit-learn==1.6.1
uvicorn app:app --reload

Then open http://127.0.0.1:8000/docs and try the /predict endpoint.
