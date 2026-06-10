import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# Load Dataset

df = pd.read_csv(r"Data\featured_uber.csv")


# Select Features (X)

X = df[
    [
        "passenger_count",
        "hour",
        "day",
        "month",
        "weekday",
        "distance"
    ]
]


# Select Target (y)

y = df["fare_amount"]


# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Check Shapes

print("X_train Shape:", X_train.shape)
print("X_test Shape :", X_test.shape)
print("y_train Shape:", y_train.shape)
print("y_test Shape :", y_test.shape)


# Create Model

model = LinearRegression()


# Train Model

model.fit(X_train, y_train)

print("\n✅ Model Trained Successfully!")


# Intercept

print("\nIntercept:")
print(model.intercept_)


# Coefficients

print("\nCoefficients:")

for feature, coefficient in zip(X.columns, model.coef_):
    print(f"{feature}: {coefficient}")


# Predictions

y_pred = model.predict(X_test)


# Evaluation Metrics

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(
    y_test,
    y_pred
)

rmse = mse ** 0.5

r2 = r2_score(
    y_test,
    y_pred
)


# Print Results

print("\n========== Model Evaluation ==========")

print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R²   :", r2)

joblib.dump(
    model,
    r"Models\uber_fare_model.pkl"
)

print("\n✅ Model Saved Successfully!")