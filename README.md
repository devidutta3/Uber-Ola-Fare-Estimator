# 🚕 Uber/Ola Fare Estimator using Machine Learning & FastAPI

## 📌 Project Overview

This project predicts Uber/Ola ride fares using Machine Learning. The model is trained on historical ride data and uses ride-related features such as passenger count, pickup time, and trip distance to estimate the fare amount.

The project includes:

* Data Cleaning
* Feature Engineering
* Haversine Distance Calculation
* Linear Regression Model
* Model Evaluation
* FastAPI REST API
* Pydantic Validation
* Swagger Documentation

---

## 🎯 Problem Statement

Ride-hailing platforms such as Uber and Ola determine fares based on multiple factors including trip distance, time, and ride details.

The objective of this project is to build a Machine Learning model capable of estimating ride fares based on available trip information.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-Learn
* FastAPI
* Pydantic
* Joblib
* Uvicorn

---

## 📂 Project Structure

```text
Uber-Ola-Fare-Estimator/

├── Data/
│   ├── cleaned_uber.csv
│   └── featured_uber.csv
│
├── Models/
│   └── uber_fare_model.pkl
│
├── engine/
│   └── main.py
│
├── data_cleaning.py
├── feature_engineering.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## 📊 Data Preprocessing

### Data Cleaning

* Removed unnecessary columns:

  * Unnamed: 0
  * key

* Removed null values using:

```python
dropna()
```

* Removed negative fare values.

---

### Feature Engineering

Extracted the following datetime features:

* Hour
* Day
* Month
* Weekday

Generated trip distance using the Haversine Formula.

---

## 🌍 Haversine Formula

The Haversine Formula calculates the great-circle distance between two points on Earth using latitude and longitude coordinates.

Generated Feature:

```text
distance
```

Distance is measured in kilometers.

---

## 🚨 Outlier Removal

Removed unrealistic trips:

```python
df = df[df["distance"] > 0]
df = df[df["distance"] <= 100]
```

This improved model performance significantly by eliminating extreme distance values.

---

## 🤖 Machine Learning Model

### Algorithm

Linear Regression

### Input Features

* passenger_count
* hour
* day
* month
* weekday
* distance

### Target Variable

```text
fare_amount
```

---

## 📈 Model Performance

| Metric   | Value |
| -------- | ----- |
| MAE      | 2.40  |
| RMSE     | 5.03  |
| R² Score | 0.73  |

### Interpretation

* Average prediction error is approximately ₹2.40.
* Typical prediction error is approximately ₹5.03.
* The model explains approximately 73% of fare variation.

---

## 💾 Model Serialization

The trained model is saved using Joblib.

```python
joblib.dump(model, "Models/uber_fare_model.pkl")
```

Saved Model:

```text
Models/uber_fare_model.pkl
```

---

## 🚀 FastAPI Integration

The trained model is exposed through a REST API built using FastAPI.

### Run the API

```bash
python -m uvicorn engine.main:app --reload
```

---

## 📚 API Documentation

FastAPI automatically generates Swagger UI documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Uber Fare Estimator API is Running 🚕"
}
```

---

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Predict Fare

```http
POST /predict
```

Request:

```json
{
  "passenger_count": 2,
  "hour": 18,
  "day": 10,
  "month": 6,
  "weekday": 2,
  "distance": 5
}
```

Response:

```json
{
  "predicted_fare": 15.01
}
```

---

## 🔍 Future Improvements

* Random Forest Regressor
* XGBoost Regressor
* Hyperparameter Tuning
* Model Deployment on Cloud
* Frontend Integration
* Real-Time Fare Prediction

---

## 👨‍💻 Author

Krishna

B.Tech Student | Frontend Developer | Machine Learning Enthusiast

GitHub: Add your GitHub profile link here.
YouTube: CodeUdaan
