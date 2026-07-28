# 🍔 Food Delivery Time Prediction

### End-to-End Machine Learning Regression • MLflow • Streamlit • Docker

> **Predict food delivery time in minutes using delivery-partner, location, traffic, weather, vehicle, order, and time-related information.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-Tuned-9ACD32?style=for-the-badge)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge\&logo=mlflow\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)

</p>

<p align="center">

**🏆 Final Model:** LightGBM Regressor (Tuned)
**📈 R² Score:** 0.7935
**⏱️ MAE:** 3.3995 minutes
**📉 RMSE:** 4.2554 minutes

</p>

---

## 🚀 Live Demo

### 🍔 [Open the Food Delivery Time Prediction App](https://akhlaque03-food-delivery-time-prediction.streamlit.app/)

Enter delivery, location, traffic, weather, vehicle, order, and timing information to receive an estimated food delivery time.

---

## 📌 Project Snapshot

|                           | Details                                  |
| ------------------------- | ---------------------------------------- |
| 🎯 Problem                | Food Delivery Time Prediction            |
| 🤖 Problem Type           | Supervised Machine Learning — Regression |
| 📊 Dataset                | 45,593 delivery records                  |
| 🏆 Final Model            | Tuned LightGBM Regressor                 |
| 📈 R² Score               | **0.7935**                               |
| 🎯 MAE                    | **3.3995 minutes**                       |
| 📉 RMSE                   | **4.2554 minutes**                       |
| 🧪 Experiment Tracking    | MLflow                                   |
| 🎛️ Hyperparameter Tuning | RandomizedSearchCV                       |
| 🌐 Web Application        | Streamlit                                |
| 🐳 Containerization       | Docker                                   |
| ☁️ Deployment             | Streamlit Community Cloud                |

---

## 💡 Why This Project?

Food delivery time depends on multiple real-world factors such as:

* 🚴 Delivery-partner characteristics
* 📍 Restaurant and customer locations
* 🌦️ Weather conditions
* 🚦 Road traffic density
* 🛵 Vehicle condition
* 🍱 Type of order
* 🎉 Festival conditions
* 🏙️ City
* ⏰ Order and pickup timing
* 📦 Multiple deliveries

The objective of this project is to build a Machine Learning regression system capable of estimating delivery time in **minutes** from these factors.

---

# 🎯 Business Problem

For a food-delivery platform, accurate delivery-time estimation can improve:

* Customer experience
* ETA accuracy
* Delivery-partner allocation
* Operational planning
* Logistics management
* Restaurant coordination

The model predicts:

```text
Estimated Food Delivery Time → Minutes
```

---

# 🔄 End-to-End Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Encoding & Scaling
     ↓
Train / Test Split
     ↓
Baseline Model Training
     ↓
Model Comparison
     ↓
Hyperparameter Tuning
     ↓
MLflow Experiment Tracking
     ↓
Final Model Selection
     ↓
Model Persistence
     ↓
Streamlit Application
     ↓
Docker Containerization
     ↓
Cloud Deployment
```

---

# 📊 Dataset

The project uses **45,593 historical food-delivery records** containing numerical and categorical information related to delivery operations.

## 🎯 Target Variable

```text
Time_taken(min)
```

The target represents the total delivery time in minutes.

## 🔑 Main Features

| Feature                       | Description                 |
| ----------------------------- | --------------------------- |
| `Delivery_person_ID`          | Delivery-partner identifier |
| `Delivery_person_Age`         | Delivery-partner age        |
| `Delivery_person_Ratings`     | Delivery-partner rating     |
| `Restaurant_latitude`         | Restaurant latitude         |
| `Restaurant_longitude`        | Restaurant longitude        |
| `Delivery_location_latitude`  | Customer latitude           |
| `Delivery_location_longitude` | Customer longitude          |
| `Order_Date`                  | Order date                  |
| `Time_Orderd`                 | Order placement time        |
| `Time_Order_picked`           | Pickup time                 |
| `Weatherconditions`           | Weather condition           |
| `Road_traffic_density`        | Traffic condition           |
| `Vehicle_condition`           | Vehicle condition           |
| `Type_of_order`               | Type of food order          |
| `Type_of_vehicle`             | Delivery vehicle            |
| `multiple_deliveries`         | Number of deliveries        |
| `Festival`                    | Festival indicator          |
| `City`                        | Delivery city               |

---

# 🧹 Data Cleaning & Preprocessing

The raw dataset contained inconsistent values, missing values, mixed data types, and extreme observations.

### Data Cleaning

* Removed the unnecessary `ID` column.
* Replaced invalid values such as `NaN ` with actual missing values.
* Converted numerical columns into appropriate numeric types.
* Converted `Order_Date` into datetime format.
* Converted order and pickup times into datetime features.
* Removed the original date/time columns after extracting useful information.

### Missing Value Treatment

| Data Type            | Treatment         |
| -------------------- | ----------------- |
| Numerical features   | Median imputation |
| Categorical features | Mode imputation   |

### Outlier Treatment

IQR-based clipping was applied to selected numerical features to reduce the effect of extreme observations while retaining the original records.

### Encoding

**Frequency Encoding**

```text
Delivery_person_ID
```

**One-Hot Encoding**

```text
Weatherconditions
Road_traffic_density
Type_of_order
Type_of_vehicle
Festival
City
```

### Feature Scaling

Numerical features were scaled after categorical encoding to ensure that scale-sensitive algorithms could operate effectively.

---

# ⚙️ Feature Engineering

Date and time information was transformed into model-ready numerical features.

### 📅 Date Features

```text
Order_Day
Order_Month
Order_Day_of_Week
```

### ⏰ Time Features

```text
Order_Hour
Order_Minute
Pickup_Hour
Pickup_Minute
```

These engineered features allow the models to capture patterns related to different days, hours, and delivery periods.

---

# 🤖 Baseline Model Comparison

Multiple regression algorithms were trained before hyperparameter optimization.

| Model             |       MAE |        MSE |      RMSE |  R² Score |
| ----------------- | --------: | ---------: | --------: | --------: |
| 🥇 **CatBoost**   | **3.480** | **19.091** | **4.369** | **0.782** |
| XGBoost           |     3.515 |     19.517 |     4.418 |     0.777 |
| LightGBM          |     3.576 |     20.197 |     4.494 |     0.770 |
| Random Forest     |     3.745 |     23.198 |     4.816 |     0.735 |
| Gradient Boosting |     4.074 |     26.522 |     5.150 |     0.698 |
| Linear Regression |     4.993 |     40.017 |     6.326 |     0.544 |
| Decision Tree     |     4.901 |     43.285 |     6.579 |     0.506 |
| KNN Regressor     |     5.576 |     50.265 |     7.090 |     0.427 |
| SVM Regressor     |     5.571 |     50.404 |     7.100 |     0.425 |

### 📌 Baseline Finding

**CatBoost** achieved the strongest baseline performance with:

```text
R²   = 0.782
MAE  = 3.480 minutes
RMSE = 4.369 minutes
```

However, the top boosting models were further optimized to determine whether performance could be improved.

### 📊 Baseline Model Comparison

![Baseline Model Comparison](screenshorts/baseline_model_comparison.png)

### 📈 Baseline Model Performance

![Baseline Model Graph](screenshorts/baseline_model_graph.png)

---

# 🎛️ Hyperparameter Tuning

The strongest boosting candidates were selected for further optimization:

* XGBoost
* LightGBM
* CatBoost

Hyperparameter tuning was performed using:

```text
RandomizedSearchCV
```

### Tuning Configuration

```text
Search Strategy : RandomizedSearchCV
Iterations      : 40
Cross Validation: 5-Fold
Scoring         : R²
Random State    : 42
Parallel Jobs   : -1
```

For LightGBM, the tuning process explored parameters such as:

```text
n_estimators
learning_rate
max_depth
num_leaves
min_child_samples
subsample
colsample_bytree
reg_alpha
reg_lambda
```

---

# 🏆 Final Model Selection

After hyperparameter tuning, the optimized models were compared using the same evaluation metrics.

| Model                 |        MAE |         MSE |       RMSE |   R² Score |
| --------------------- | ---------: | ----------: | ---------: | ---------: |
| 🥇 **LightGBM Tuned** | **3.3995** | **18.1084** | **4.2554** | **0.7935** |
| XGBoost Tuned         |     3.4394 |     18.6834 |     4.3224 |     0.7869 |
| CatBoost Tuned        |     3.4520 |     18.9816 |     4.3568 |     0.7835 |

### 🥇 Selected Deployment Model

# LightGBM Regressor — Tuned

The tuned LightGBM model achieved the best overall performance and was selected for deployment.

### Final Performance

| Metric       |             Result |
| ------------ | -----------------: |
| **R² Score** |         **0.7935** |
| **MAE**      | **3.3995 minutes** |
| **MSE**      |        **18.1084** |
| **RMSE**     | **4.2554 minutes** |

### 📈 What This Means

The model explains approximately **79.35% of the variance** in delivery time on the evaluation data.

The average absolute prediction error is approximately **3.4 minutes**, while the RMSE is approximately **4.26 minutes**.

### 📊 Tuned Model Comparison

![Tuned Model Comparison](screenshorts/tuned_model_comparison.png)

### 📈 Tuned Model Performance

![Tuned Model Graph](screenshorts/tuned_model_graph.png)

### 🏆 Final LightGBM Metrics

![LightGBM Tuned Metrics](screenshorts/lightgbm_tuned_metrics.png)

---

# 🔍 Feature Importance

The final LightGBM model was analyzed to identify the features contributing most strongly to predictions.

### Top Important Features

| Rank | Feature                       | Importance |
| ---: | ----------------------------- | ---------: |
|    1 | `Order_Day`                   |       4617 |
|    2 | `Delivery_location_latitude`  |       3844 |
|    3 | `Delivery_person_ID`          |       3652 |
|    4 | `Delivery_location_longitude` |       3387 |
|    5 | `Restaurant_longitude`        |       3381 |
|    6 | `Delivery_person_Age`         |       3375 |
|    7 | `Restaurant_latitude`         |       3258 |
|    8 | `Order_Hour`                  |       2954 |
|    9 | `Delivery_person_Ratings`     |       2515 |
|   10 | `Pickup_Hour`                 |       2362 |

### 📊 Feature Importance Visualization

The application also provides a visual representation of the top features used by the final model.

---

# 🧪 MLflow Experiment Tracking

**MLflow** was integrated into the project to track Machine Learning experiments and improve reproducibility.

### MLflow Used For

* Experiment tracking
* Model parameters
* Evaluation metrics
* Baseline model runs
* Tuned model experiments
* Model comparison
* Model selection workflow

### Experiment

```text
Food_Delivery_Prediction
```

### 📊 MLflow Experiment Tracking

![MLflow Experiment Tracking](screenshorts/mlflow_experiment_tracking.png)

> MLflow was used during local development to organize and track experiments. The local MLflow database is intentionally excluded from version control.

---

# 💾 Model Persistence

The final trained model and preprocessing artifacts are stored separately for inference.

| Artifact                           | Purpose                           |
| ---------------------------------- | --------------------------------- |
| `Food_Delivery_LightGBM_Tuned.pkl` | Final tuned LightGBM model        |
| `feature_columns.pkl`              | Required feature-column structure |
| `freq_mappings.pkl`                | Frequency-encoding mappings       |

The Streamlit application loads these artifacts to reproduce the required preprocessing and generate predictions.

---

# 🌐 Streamlit Application

The trained model was integrated into an interactive Streamlit application.

### Application Features

* 🎛️ Interactive input controls
* 🚴 Delivery-partner information
* 📍 Restaurant and delivery location
* 🌦️ Weather conditions
* 🚦 Traffic density
* 🛵 Vehicle information
* 🍱 Order information
* 🎉 Festival information
* ⏰ Order and pickup timing
* 🤖 Real-time model prediction
* 📊 Model performance information
* 🔍 Feature importance visualization

### 🏠 Application Home Page

![Streamlit Home Page](screenshorts/home_page.png)

### 🎯 Prediction Result

![Prediction Result](screenshorts/prediction_result.png)

### 🚀 Live Application

**[🍔 Launch Food Delivery Time Prediction](https://akhlaque03-food-delivery-time-prediction.streamlit.app/)**

---

# 🐳 Docker Containerization

The Streamlit application was containerized using Docker to provide a consistent and reproducible runtime environment.

### Build Docker Image

```bash
docker build -t food-delivery-app .
```

### Run Docker Container

```bash
docker run -p 8501:8501 food-delivery-app
```

### 🐳 Docker Container Running

![Docker Container](screenshorts/docker_container_running.png)

---

# 🖥️ Run Locally

## 1. Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Food-Delivery-Time-Prediction
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Environment — Windows

```bash
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run Streamlit

```bash
streamlit run app.py
```

The application will open locally in your browser.

---

# 🧪 Run MLflow Locally

If you want to inspect the locally tracked MLflow experiments:

```bash
mlflow ui
```

Then open:

```text
http://127.0.0.1:5000
```

---

# 🛠️ Tech Stack

### Programming

* Python 3.13

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* XGBoost
* LightGBM
* CatBoost

### Visualization

* Matplotlib
* Seaborn

### Experiment Tracking

* MLflow

### Application

* Streamlit

### Deployment & DevOps

* Docker
* Streamlit Community Cloud

### Development

* Jupyter Notebook
* VS Code

---

# 📁 Project Structure

```text
Food-Delivery-Time-Prediction/
│
├── app.py
├── train.csv
├── requirements.txt
├── runtime.txt
├── Dockerfile
│
├── Food_Delivery_LightGBM_Tuned.pkl
├── feature_columns.pkl
├── freq_mappings.pkl
│
├── README.md
│
└── screenshorts/
    ├── baseline_model_comparison.png
    ├── baseline_model_graph.png
    ├── docker_container_running.png
    ├── home_page.png
    ├── lightgbm_tuned_metrics.png
    ├── mlflow_experiment_tracking.png
    ├── prediction_result.png
    ├── tuned_model_comparison.png
    └── tuned_model_graph.png
```

---

# 📈 Key Takeaways

### Baseline → Tuned Model

The project demonstrates a complete model-improvement process:

```text
Best Baseline
CatBoost
R² = 0.782
        ↓
Hyperparameter Tuning
        ↓
Best Tuned Model
LightGBM
R² = 0.7935
```

### Performance Improvement

| Metric | Baseline CatBoost | Tuned LightGBM | Improvement |
| ------ | ----------------: | -------------: | ----------: |
| R²     |            0.7823 |     **0.7935** |           ↑ |
| MAE    |            3.4801 |     **3.3995** |           ↓ |
| RMSE   |            4.3693 |     **4.2554** |           ↓ |
| MSE    |           19.0910 |    **18.1084** |           ↓ |

The tuned LightGBM model improved upon the strongest baseline and was therefore selected for deployment.

---

# 🚀 Deployment Status

| Component                 | Status      |
| ------------------------- | ----------- |
| Data Cleaning             | ✅ Completed |
| EDA                       | ✅ Completed |
| Feature Engineering       | ✅ Completed |
| Preprocessing             | ✅ Completed |
| Baseline Model Comparison | ✅ Completed |
| Hyperparameter Tuning     | ✅ Completed |
| MLflow Tracking           | ✅ Completed |
| Final Model Selection     | ✅ Completed |
| Model Persistence         | ✅ Completed |
| Streamlit Application     | ✅ Completed |
| Docker Containerization   | ✅ Completed |
| Cloud Deployment          | ✅ Completed |

---

# 🔮 Future Improvements

Potential next steps include:

* 🌍 Geospatial distance and route-based features
* 🌦️ Real-time weather API integration
* 🚦 Real-time traffic API integration
* 🔎 SHAP-based model explainability
* 🔄 Automated model retraining
* 📊 Production model monitoring
* ⚙️ CI/CD automation
* ☁️ AWS / Azure / GCP deployment
* 🧪 Automated testing pipeline
* 📈 Continuous performance monitoring

---

# 👨‍💻 Author

## Akhlaque Alam

**Aspiring Data Scientist | Machine Learning | Python | SQL | Streamlit | MLflow | Docker**

I enjoy building practical Machine Learning solutions, transforming real-world datasets into predictive systems, and deploying models as usable applications.

### 🔗 Project

**Live Demo:**
https://akhlaque03-food-delivery-time-prediction.streamlit.app/

---

<p align="center">

### ⭐ If you found this project useful, consider giving the repository a star!

</p>
