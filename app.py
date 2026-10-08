from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput 
from typing import Literal, Annotated
import pickle
import pandas as pd
from model.predict import predict_output, model , MODEL_VERSION 


# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'


app = FastAPI()

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]





@app.get('/')
def home():
    return{'message': " Insurance Premium Prediction API "}

@app.get('/health')
def health_check():
    return {
        'status': 'ok',
        'version': MODEL_VERSION
    }


@app.post('/predict')
def predict_premium(data: UserInput):
    user_input = ([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,   # property, so no ()
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,
    }])

    prediction = predict_output([user_input])

    return JSONResponse(status_code=200, content={'predicted_category': str(prediction)})

