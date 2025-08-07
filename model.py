import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv("environment_data.csv")

X = df[["Temperature", "Humidity", "WindSpeed"]]
y = df["AirQualityIndex"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = ElasticNet(alpha=0.1, l1_ratio=0.5)
model.fit(X_train, y_train)

joblib.dump(model, "elastic_model.pkl")
joblib.dump(scaler, "scaler.pkl")
