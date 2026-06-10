import pandas as pd
import math


def load_dataset(path):
    return pd.read_csv(path)


def convert_date_time(df):
    df["pickup_datetime"] = pd.to_datetime(
        df["pickup_datetime"]
    )

    return df


def extract_datetime_features(df):
    df["hour"] = df["pickup_datetime"].dt.hour
    df["day"] = df["pickup_datetime"].dt.day
    df["month"] = df["pickup_datetime"].dt.month
    df["weekday"] = df["pickup_datetime"].dt.weekday

    return df


def haversine_distance(
    pickup_lat,
    pickup_lon,
    dropoff_lat,
    dropoff_lon
):
    R = 6371

    pickup_lat = math.radians(pickup_lat)
    pickup_lon = math.radians(pickup_lon)

    dropoff_lat = math.radians(dropoff_lat)
    dropoff_lon = math.radians(dropoff_lon)

    dlat = dropoff_lat - pickup_lat
    dlon = dropoff_lon - pickup_lon

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(pickup_lat)
        * math.cos(dropoff_lat)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return R * c


def calculate_distance(df):
    df["distance"] = df.apply(
        lambda row: haversine_distance(
            row["pickup_latitude"],
            row["pickup_longitude"],
            row["dropoff_latitude"],
            row["dropoff_longitude"]
        ),
        axis=1
    )

    return df


def save_dataset(df, path):
    df.to_csv(path, index=False)


# Load Dataset
df = load_dataset(r"Data\cleaned_uber.csv")

# Convert Datetime
df = convert_date_time(df)

# Extract Datetime Features
df = extract_datetime_features(df)

# Calculate Distance
df = calculate_distance(df)

# Save Engineered Dataset
save_dataset(df, r"Data\featured_uber.csv")

# Preview
print(df.head())

print("\nNew Features:")
print(df[["hour", "day", "month", "weekday", "distance"]].head())