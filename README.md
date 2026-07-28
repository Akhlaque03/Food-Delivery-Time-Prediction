# 🍔 Food Delivery Time Prediction

### End-to-End Machine Learning Regression Project

Predicting food delivery time in minutes using delivery-partner information, location, weather, traffic, vehicle condition, order details, festival status, and time-related features.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-orange?style=for-the-badge)
![LightGBM](https://img.shields.io/badge/LightGBM-4.6.0-9ACD32?style=for-the-badge)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-0194E2?style=for-the-badge\&logo=mlflow\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)

</p>

---

## 🚀 Live Demo

### 🍔 [Open Food Delivery Time Prediction App](https://akhlaque03-food-delivery-time-prediction.streamlit.app/)

Enter delivery-related information and get an estimated delivery time directly from the trained Machine Learning model.

---

## 📌 Project Overview

**Food Delivery Time Prediction** is an end-to-end Machine Learning regression project built around a real-world delivery-time prediction problem.

The objective is to estimate how many minutes a food order will take to reach the customer using information such as:

* Delivery-partner characteristics
* Restaurant and customer locations
* Weather conditions
* Road traffic density
* Vehicle condition
* Order details
* Festival status
* City
* Order and pickup timing

The project covers the complete journey from **raw data to a live deployed Machine Learning application**.

### 🔄 Complete Project Lifecycle

**Data → Cleaning → EDA → Feature Engineering → Preprocessing → Model Training → MLflow Tracking → Hyperparameter Tuning → Model Selection → Model Registry → Model Persistence → Streamlit → Docker → Cloud Deployment**

---

## 🎯 Business Problem

Food delivery time is affected by several dynamic factors, including traffic, weather, delivery-partner experience, vehicle condition, location, order characteristics, and time of day.

Accurate delivery-time estimation can help food-delivery platforms improve:

* Customer experience
* Estimated delivery-time accuracy
* Delivery-partner allocation
* Operational planning
* Restaurant and logistics management

This project builds a regression model that predicts the expected delivery time in **minutes**.

---

## ⭐ Why This Project Stands Out

* End-to-end Machine Learning implementation
* Real-world regression problem
* Multiple regression algorithms compared
* Advanced boosting models tuned
* MLflow used for experiment tracking
* Model Registry included in the workflow
* Saved model and preprocessing artifacts
* Interactive Streamlit application
* Docker containerization
* Cloud deployment with live demo
* Reproducible local setup

---

## 🔄 Machine Learning Workflow

The project follows a structured production-oriented workflow:

| Stage                    | Implementation                                          |
| ------------------------ | ------------------------------------------------------- |
| 📊 Dataset               | Historical food-delivery data                           |
| 🧹 Data Cleaning         | Missing values, invalid entries, data types             |
| 🔎 EDA                   | Target distribution, categorical analysis, correlations |
| ⚙️ Feature Engineering   | Date and time-based features                            |
| 🔄 Preprocessing         | Frequency encoding, one-hot encoding, scaling           |
| 🤖 Model Training        | Multiple regression algorithms                          |
| 📊 MLflow Tracking       | Parameters, metrics, model runs                         |
| 🎯 Hyperparameter Tuning | XGBoost, LightGBM, CatBoost                             |
| 🏆 Model Selection       | Tuned-model comparison                                  |
| 🗂️ Model Registry       | Selected model registration                             |
| 💾 Model Persistence     | `.pkl` model and preprocessing artifacts                |
| 🌐 Streamlit             | Interactive prediction application                      |
| 🐳 Docker                | Containerized deployment                                |
| ☁️ Cloud Deployment      | Live Streamlit Community Cloud application              |

---

## 📊 Dataset

The dataset contains **45,593 historical food-delivery records** with numerical and categorical features.

### 🎯 Target Variable

```text
Time_taken(min)
```

**Target:** Food delivery time in minutes.

### 🔑 Important Features

| Feature                       | Description                  |
| ----------------------------- | ---------------------------- |
| `Delivery_person_ID`          | Delivery partner identifier  |
| `Delivery_person_Age`         | Age of delivery partner      |
| `Delivery_person_Ratings`     | Delivery partner rating      |
| `Restaurant_latitude`         | Restaurant latitude          |
| `Restaurant_longitude`        | Restaurant longitude         |
| `Delivery_location_latitude`  | Customer latitude            |
| `Delivery_location_longitude` | Customer longitude           |
| `Order_Date`                  | Order date                   |
| `Time_Orderd`                 | Order placement time         |
| `Time_Order_picked`           | Order pickup time            |
| `Weatherconditions`           | Weather condition            |
| `Road_traffic_density`        | Traffic condition            |
| `Vehicle_condition`           | Vehicle condition            |
| `Type_of_order`               | Food order type              |
| `Type_of_vehicle`             | Delivery vehicle             |
| `multiple_deliveries`         | Number of deliveries handled |
| `Festival`                    | Festival indicator           |
| `City`                        | Delivery city                |

---

## 🧹 Data Cleaning & Preprocessing

The raw dataset contained missing values, inconsistent strings, mixed data types, and extreme values.

### Data Cleaning

* Removed the unnecessary `ID` column.
* Replaced invalid values such as `NaN ` with actual missing values.
* Converted numerical columns to appropriate numeric types.
* Converted `Order_Date` into datetime format.
* Converted order and pickup times into datetime features.
* Removed original date/time columns after feature extraction.

### Missing Value Treatment

* Numerical features → **Median imputation**
* Categorical features → **Mode imputation**

### Outlier Treatment

Extreme numerical values were handled using **IQR-based clipping** to reduce the impact of unusually large or small observations while retaining the original records.

### Preprocessing

* Frequency encoding for `Delivery_person_ID`
* One-hot encoding for categorical variables
* Numerical feature scaling
* Train-test split before model training

---

## ⚙️ Feature Engineering

Feature engineering was used to extract meaningful information from raw date and time fields.

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

### 🔤 Encoding Strategy

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

### 📏 Feature Scaling

Numerical features were scaled after encoding so that algorithms sensitive to feature magnitude could operate effectively.

---

## 🤖 Machine Learning Models

Multiple regression algorithms were trained and compared.

### Baseline Models

* Linear Regression
* KNN Regressor
* SVM Regressor
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor
* LightGBM Regressor
* CatBoost Regressor

### 🎯 Hyperparameter Tuning

The strongest boosting candidates were further optimized:

* XGBoost
* LightGBM
* CatBoost

The tuned models were compared using the same evaluation metrics before selecting the final deployment model.

---

## 📈 Model Evaluation

The models were evaluated using:

| Metric       | Purpose                           |
| ------------ | --------------------------------- |
| **R² Score** | Measures explained variance       |
| **MAE**      | Average absolute error in minutes |
| **MSE**      | Average squared prediction error  |
| **RMSE**     | Prediction error in minutes       |

### Baseline Model Comparison

| Model             |   R² Score |        MAE |       RMSE |
| ----------------- | ---------: | ---------: | ---------: |
| Linear Regression |   -49.4815 |    65.3959 |    66.5291 |
| KNN Regressor     |    -0.0839 |     7.8676 |     9.7487 |
| SVM Regressor     |    -0.0923 |     8.1408 |     9.7864 |
| Decision Tree     |     0.5063 |     4.9011 |     6.5791 |
| Random Forest     |     0.7354 |     3.7452 |     4.8164 |
| Gradient Boosting |     0.6975 |     4.0741 |     5.1499 |
| XGBoost           |     0.7774 |     3.5153 |     4.4178 |
| LightGBM          |     0.7696 |     3.5760 |     4.4941 |
| **CatBoost**      | **0.7823** | **3.4801** | **4.3693** |

> **Note:** These are baseline results before hyperparameter tuning. The final deployment model was selected after tuned-model comparison.

### 📊 Baseline Model Comparison

![Baseline Model Comparison](screenshorts/baseline_model_comparison.png)

### 📈 Baseline Model Graph

![Baseline Model Graph](screenshorts/baseline_model_graph.png)

---

## 🏆 Hyperparameter Tuning & Final Model

After baseline comparison, hyperparameter tuning was performed on:

* XGBoost
* LightGBM
* CatBoost

The tuned models were evaluated using:

**R² Score · MAE · MSE · RMSE**

### 🥇 Final Deployment Model

**LightGBM Tuned** was selected as the final deployment model based on the tuned-model comparison.

### Why LightGBM?

LightGBM was selected because it provided strong predictive performance while maintaining efficient training and inference.

The final trained model is stored as:

```text
Food_Deliver_lightgbm.pkl
```

### 📊 Tuned Model Comparison

![Tuned Model Comparison](screenshorts/tuned_model_comparison.png)

### 📈 Tuned Model Graph

![Tuned Model Graph](screenshorts/tuned_model_graph.png)

---

## 📊 MLflow Experiment Tracking

[MLflow](https://mlflow.org/) was used to track Machine Learning experiments throughout the project.

### Tracked Information

* Model runs
* Model parameters
* Evaluation metrics
* Baseline model results
* Tuned model experiments
* Final model performance

### Experiment Name

```text
Food_Delivery_Prediction
```

### MLflow Experiment Tracking

![MLflow Experiment Tracking](screenshorts/mlflow_experiment_tracking.png)

> `mlflow.db` is used as the local MLflow database backend and is kept out of version control.

---

## 🧠 Model & Preprocessing Artifacts

The trained model and preprocessing information are stored separately so the same transformations used during training can be reproduced during inference.

| File                        | Purpose                                               |
| --------------------------- | ----------------------------------------------------- |
| `Food_Deliver_lightgbm.pkl` | Final trained LightGBM regression model               |
| `feature_columns.pkl`       | Feature-column structure required during inference    |
| `freq_mappings.pkl`         | Frequency-encoding mappings used during preprocessing |

These artifacts are loaded by the Streamlit application to prepare user inputs and generate predictions.

---

## 🌐 Streamlit Application

The final LightGBM model was integrated into an interactive **Streamlit** application.

### Application Features

* Interactive prediction form
* Delivery-partner information
* Restaurant and customer location details
* Weather and traffic conditions
* Vehicle and order information
* Festival and city information
* Real-time delivery-time prediction

### 🏠 Streamlit Home Page

![Streamlit Home Page](screenshorts/home_page.png)

### 🎯 Prediction Result

![Prediction Result](screenshorts/prediction_result.png)

### 🚀 Live Application

**[🍔 Open Food Delivery Time Prediction App](https://akhlaque03-food-delivery-time-prediction.streamlit.app/)**

---

## 🐳 Docker Deployment

## 🐳 Docker Deployment

The Streamlit application was containerized using Docker to provide a consistent and reproducible deployment environment.

### Docker Configuration

The project includes a `Dockerfile` configured to run the Streamlit application.

### Build Docker Image

```bash
docker build -t food-delivery-app .
```

### Run Docker Container

```bash
docker run -p 8501:8501 food-delivery-app
```

### Docker Container Screenshot

![Docker Container](screenshorts/docker_container_running.png)

---


---

## 🖥️ Local Setup & Installation

### 1. Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Food-Delivery-Time-Prediction
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment — Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Streamlit

```bash
streamlit run app.py
```

---

## 📊 Run MLflow Locally

The project uses SQLite as the local MLflow backend.

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

MLflow UI will normally be available at:

```text
http://127.0.0.1:5000
```

---

## 🛠️ Technologies & Tools

### Programming Language

* Python 3.13

### Data Science & Machine Learning

* Pandas
* NumPy
* Scikit-learn
* XGBoost
* LightGBM
* CatBoost

### Data Visualization

* Matplotlib
* Seaborn

### Experiment Tracking

* MLflow

### Application

* Streamlit

### Deployment & DevOps

* Docker
* Streamlit Community Cloud

### Development Environment

* Jupyter Notebook
* VS Code

---

## 📁 Project Structure

```text
Food-Delivery-Time-Prediction/
│
├── app.py
├── train.csv
├── requirements.txt
├── runtime.txt
├── Dockerfile
│
├── Food_Deliver_lightgbm.pkl
├── feature_columns.pkl
├── freq_mappings.pkl
│
├── mlflow.db
├── README.md
│
└── screenshorts/
    ├── baseline_model_comparison.png
    ├── baseline_model_graph.png
    ├── tuned_model_comparison.png
    ├── tuned_model_graph.png
    ├── home_page.png
    ├── prediction_result.png
    ├── mlflow_experiment_tracking.png
    ├── lightgbm_tuned_metrics.png
    └── docker_container_running.png
```

---

## 📌 Final Results

### Baseline Performance

The strongest baseline performance was achieved by **CatBoost**:

| Metric       |              Score |
| ------------ | -----------------: |
| **R² Score** |         **0.7823** |
| **MAE**      | **3.4801 minutes** |
| **RMSE**     | **4.3693 minutes** |

The final deployment model was selected after hyperparameter tuning and tuned-model comparison.

### Deployment Completed

* ✅ Machine Learning regression model trained
* ✅ Multiple models compared
* ✅ Hyperparameter tuning completed
* ✅ MLflow experiment tracking implemented
* ✅ Model Registry workflow implemented
* ✅ Model and preprocessing artifacts saved
* ✅ Streamlit application developed
* ✅ Docker containerization completed
* ✅ Application deployed to Streamlit Community Cloud
* ✅ Live prediction application available

### 🚀 Live Project

**[🍔 View Live Food Delivery Time Prediction App](https://akhlaque03-food-delivery-time-prediction.streamlit.app/)**

---

## 🚀 Future Improvements

Potential improvements include:

* Real-time traffic and weather API integration
* Geospatial distance and route-based features
* Advanced ensemble and deep-learning models
* Automated model retraining pipelines
* MLflow-based production monitoring
* SHAP-based model explainability
* CI/CD automation
* Cloud deployment on AWS, Azure, or Google Cloud
* Continuous prediction-performance monitoring

---

## 👨‍💻 Author

### Akhlaque Alam

**Aspiring Data Scientist | Machine Learning | Python | SQL | Streamlit | MLflow | Docker**

Passionate about building practical Machine Learning solutions, deploying data-driven applications, and turning real-world datasets into useful predictive systems.

---

### ⭐ If you found this project interesting, feel free to explore the repository and try the live application.
