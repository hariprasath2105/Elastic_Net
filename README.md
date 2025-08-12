# Air Quality Prediction using Elastic Net Regression

This project uses **Elastic Net Regression** to predict the **Air Quality Index (AQI)** based on three key environmental features.

## Dataset

The dataset `environment_data.csv` contains the following columns:

- `Temperature` (°C)
- `Humidity` (%)
- `WindSpeed` (m/s)
- `AirQualityIndex` (target)

---

## Model

We used the `ElasticNet` model from `sklearn.linear_model` to predict AQI.

### Features Used:
- Temperature
- Humidity
- Wind Speed

### Target:
- Air Quality Index

The model was trained using `scikit-learn`, scaled with `StandardScaler`, and saved using `pickle`.

---
## Tech Stack

| Technology     | Use                  |
|----------------|----------------------|
| Python         | Core language        |
| scikit-learn   | Machine Learning     |
| Pandas         | Data manipulation    |
| Gradio         | Web-based UI         |

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-FF6B81?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---
## Project Structure

```
elastic_net_app/
│
├── environment_data.csv       
├── model.py                     
├── app.py                       
├── elastic_model.pkl           
└── scaler.pkl                   
```

---

## Run the App

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

## How to Use the App

Adjust the following sliders:
- **Temperature (25°C to 40°C)**
- **Humidity (30% to 70%)**
- **Wind Speed (0 to 10 m/s)**

The model will predict the **Air Quality Index** based on these values.

---

## Smaple UI

**Input**:

<img width="1292" height="352" alt="image" src="https://github.com/user-attachments/assets/90532c99-9ba4-4214-82ab-ccd282f2024d" />

**Output**:

<img width="1292" height="353" alt="image" src="https://github.com/user-attachments/assets/a6a24825-8641-4043-b91d-eb1dddf0d7c4" />

---
