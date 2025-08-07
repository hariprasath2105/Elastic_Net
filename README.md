# 🌿 Air Quality Prediction using Elastic Net Regression

This project uses **Elastic Net Regression** to predict the **Air Quality Index (AQI)** based on three key environmental features.

## 📁 Dataset

The dataset `environment_data.csv` contains the following columns:

- `Temperature` (°C)
- `Humidity` (%)
- `WindSpeed` (m/s)
- `AirQualityIndex` (target)

📥 [Download Dataset](./environment_data.csv)

---

## 🧠 Model

We used the `ElasticNet` model from `sklearn.linear_model` to predict AQI.

### Features Used:
- Temperature
- Humidity
- Wind Speed

### Target:
- Air Quality Index

The model was trained using `scikit-learn`, scaled with `StandardScaler`, and saved using `pickle`.

---

## 💻 Project Structure

```
elastic_net_app/
│
├── environment_data.csv         # Dataset
├── model.py                     # Training and saving the model
├── app.py                       # Gradio web app
├── elastic_model.pkl            # Saved model (via pickle)
└── scaler.pkl                   # Saved scaler (via pickle)
```

---

## 🚀 Run the App

### Step 1: Train the Model

```bash
python model.py
```

### Step 2: Launch the Gradio App

```bash
python app.py
```

The app will run locally at: `http://127.0.0.1:7860`

---

## 🧪 How to Use the App

Adjust the following sliders:
- **Temperature (25°C to 40°C)**
- **Humidity (30% to 70%)**
- **Wind Speed (0 to 10 m/s)**

The model will predict the **Air Quality Index** based on these values.

---

## 📦 Dependencies

- pandas
- numpy
- scikit-learn
- gradio
- pickle

Install them using:

```bash
pip install pandas numpy scikit-learn gradio
```

---

## 📌 Author

Developed by [Your Name]