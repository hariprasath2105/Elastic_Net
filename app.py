import gradio as gr
import numpy as np
import joblib

model = joblib.load("elastic_model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_air_quality(temp, humidity, windspeed):
    input_data = np.array([[temp, humidity, windspeed]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    return f"Predicted Air Quality Index (AQI): {prediction:.2f}"

iface = gr.Interface(
    fn=predict_air_quality,
    inputs=[
        gr.Slider(25, 40, step=0.1, label="Temperature (°C)"),
        gr.Slider(30, 70, step=1, label="Humidity (%)"),
        gr.Slider(0, 10, step=0.1, label="Wind Speed (m/s)")
    ],
    outputs="text",
    title="🌿 Air Quality Index Predictor",
    description="Estimate the Air Quality Index using Elastic Net Regression.",
    theme="default"
)

iface.launch()
