from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

# Load the model
model_path = "final_model.joblib"
model = joblib.load(model_path)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",  # Allow localhost
    "http://127.0.0.1",  # Allow 127.0.0.1
    "http://localhost:8501",  # or any other relevant frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Can be a list of allowed origins or "*" for all
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define a route to serve predictions
@app.post("/predict/")
async def predict(features: dict):
    try:
        # Convert the input features to a DataFrame
        input_df = pd.DataFrame([features])
        
        # Make predictions
        prediction = model.predict(input_df)[0]
        
        # Return the prediction result
        return {"prediction": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
