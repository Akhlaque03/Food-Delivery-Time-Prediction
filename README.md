# 🍔 Food Delivery Time Prediction

A real-world **Machine Learning regression project** that predicts food delivery time in minutes based on delivery-partner information, location, weather, traffic, vehicle condition, order details, festival status, and time-related features.

The project covers the complete machine-learning workflow from **data preprocessing and feature engineering to model comparison, hyperparameter tuning, MLflow experiment tracking, Streamlit deployment, and Docker containerization**.

---

## 📌 Project Overview

Accurate delivery-time prediction can help food-delivery platforms improve:

* Customer experience
* Delivery-time estimation
* Operational planning
* Delivery-partner allocation
* Restaurant and logistics management

This project builds a regression model to predict:

> **Time Taken for Food Delivery (in minutes)**

---

## 🎯 Objective

The primary objective is to develop a machine-learning model that can predict food delivery time using historical delivery data and deploy the final model as a web application.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis (EDA)
   ↓
Feature Engineering
   ↓
Train-Test Split
   ↓
Feature Encoding & Scaling
   ↓
Baseline Model Training
   ↓
MLflow Experiment Tracking
   ↓
Hyperparameter Tuning
   ↓
Tuned Model Comparison
   ↓
Best Model Selection
   ↓
Save Model & Preprocessing Files
   ↓
Streamlit Application
   ↓
Local Testing
   ↓
Docker Containerization
```

---

## 📊 Dataset

The dataset contains information related to food delivery orders.

### Important Features

| Feature                       | Description                        |
| ----------------------------- | ---------------------------------- |
| `Delivery_person_ID`          | Unique delivery partner identifier |
| `Delivery_person_Age`         | Age of delivery partner            |
| `Delivery_person_Ratings`     | Delivery partner rating            |
| `Restaurant_latitude`         | Restaurant latitude                |
| `Restaurant_longitude`        | Restaurant longitude               |
| `Delivery_location_latitude`  | Customer delivery latitude         |
| `Delivery_location_longitude` | Customer delivery longitude        |
| `Order_Date`                  | Date of order                      |
| `Time_Orderd`                 | Order placement time               |
| `Time_Order_picked`           | Order pickup time                  |
| `Weatherconditions`           | Weather condition                  |
| `Road_traffic_density`        | Traffic condition                  |
| `Vehicle_condition`           | Vehicle condition                  |
| `Type_of_order`               | Type of food order                 |
| `Type_of_vehicle`             | Delivery vehicle                   |
| `multiple_deliveries`         | Number of deliveries               |
| `Festival`                    | Festival indicator                 |
| `City`                        | Delivery city                      |
| `Time_taken(min)`             | **Target variable**                |

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

* Removed unnecessary `ID` column.
* Replaced invalid string values such as `NaN ` with actual missing values.
* Converted numerical columns to appropriate numeric data types.
* Handled missing numerical values using **median imputation**.
* Handled missing categorical values using **mode imputation**.
* Converted `Order_Date` into datetime format.
* Extracted date-related features.
* Converted order and pickup times into useful numerical time features.
* Removed unnecessary original datetime columns after feature extraction.
* Handled extreme values using **IQR-based clipping**.

---

## ⚙️ Feature Engineering

New features were created to improve model performance.

### Date Features

```text
Order_Day
Order_Month
Order_Day_of_Week
```

### Time Features

```text
Order_Hour
Order_Minute
Pickup_Hour
Pickup_Minute
```

### Categorical Encoding

One-hot encoding was applied to relevant categorical features.

Frequency encoding was used for:

```text
Delivery_person_ID
```

### Feature Scaling

Numerical features were scaled after the encoding process.

---

## 🤖 Machine Learning Models

Several regression algorithms were trained and compared.

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

### Tuned Models

Hyperparameter tuning was performed on:

* XGBoost
* LightGBM
* CatBoost

---

## 📈 Model Evaluation

The models were evaluated using:

* **R² Score**
* **MAE**
* **MSE**
* **RMSE**

### Baseline Model Results

| Model             | R²       | MAE     | RMSE    |
| ----------------- | -------- | ------- | ------- |
| Linear Regression | -49.4815 | 65.3959 | 66.5291 |
| KNN Regressor     | -0.0839  | 7.8676  | 9.7487  |
| SVM Regressor     | -0.0923  | 8.1408  | 9.7864  |
| Decision Tree     | 0.5063   | 4.9011  | 6.5791  |
| Random Forest     | 0.7354   | 3.7452  | 4.8164  |
| Gradient Boosting | 0.6975   | 4.0741  | 5.1499  |
| XGBoost           | 0.7774   | 3.5153  | 4.4178  |
| LightGBM          | 0.7696   | 3.5760  | 4.4941  |
| CatBoost          | 0.7823   | 3.4801  | 4.3693  |

> **Note:** The baseline model comparison was performed before hyperparameter tuning. The final selected model is based on the tuned-model comparison.

---

## 🏆 Best Model

After hyperparameter tuning and model comparison, **LightGBM Tuned** was selected as the final model for deployment.

### Why LightGBM?

LightGBM was selected because it provided the strongest overall performance among the tuned candidates used for the final deployment workflow while maintaining efficient training and prediction.

The final model was saved as:

```text
Food_Deliver_lightgbm.pkl
```

---

## 📁 Project Files

```text
Food Delivery Time Prediction/
│
├── app.py
├── Dockerfile
├── feature_columns.pkl
├── Food_Deliver_lightgbm.pkl
├── freq_mappings.pkl
├── requirements.txt
├── train.csv
├── mlflow.db
├── README.md
│
└── screenshots/
    ├── baseline_model.png
    ├── baseline_model_graph.png
    ├── tuned_model.png
    ├── tuned_model_graph.png
    ├── home_page.png
    ├── prediction_result.png
    ├── mlflow_experiments.png
    ├── lightgbm_tuned_metrics.png
    └── docker_container.png
```

---

## 🧠 Saved Model & Preprocessing Files

### `Food_Deliver_lightgbm.pkl`

Contains the final trained LightGBM model used by the Streamlit application.

### `feature_columns.pkl`

Stores the feature-column structure required during prediction.

### `freq_mappings.pkl`

Stores frequency-encoding mappings used during preprocessing.

These files ensure that the same preprocessing logic used during training can be reproduced during inference.

---

## 📊 MLflow Experiment Tracking

MLflow was used to track the machine-learning experiments.

The project tracks:

* Model runs
* Model names
* Evaluation metrics
* Experiment results
* Tuned model experiments
* Final model metrics

The MLflow experiment used in the project is:

```text
Food_Delivery_Prediction
```

### MLflow Screenshots

> `mlflow.db` is used as the local MLflow database backend and is intentionally kept out of version control.

---

## 🌐 Streamlit Application

The final LightGBM model was integrated into a Streamlit web application.

The application allows users to enter delivery-related information and receive a predicted delivery time.

### Application Screenshots

#### Home Page

#### Prediction Result

---

## 🐳 Docker Deployment

The Streamlit application was containerized using Docker.

The project includes:

```text
Dockerfile
```

The Docker container runs the Streamlit application on:

```text
8501
```

### Docker Screenshot

---

## 🖥️ Run the Project Locally

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Food-Delivery-Time-Prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## 📊 Run MLflow Locally

The project uses SQLite as the MLflow backend.

From the project directory:

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Then open:

```text
http://127.0.0.1:5000
```

---

## 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t food-delivery-app .
```

Run the container:

```bash
docker run -p 8501:8501 food-delivery-app
```

Then open:

```text
http://localhost:8501
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

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

### Development Environment

* Jupyter Notebook
* VS Code / Python environment

---

## 📸 Project Screenshots

### Baseline Model

### Baseline Model Graph

### Tuned Model

### Tuned Model Graph

### Streamlit Home Page

### Prediction Result

### MLflow Experiment Tracking

### LightGBM Tuned Metrics

### Docker Container

---

## 🚀 Key Highlights

* End-to-end machine learning regression workflow.
* Real-world food delivery time prediction problem.
* Data cleaning and missing-value handling.
* IQR-based outlier treatment.
* Date and time feature engineering.
* Categorical encoding and feature scaling.
* Comparison of multiple regression algorithms.
* Hyperparameter tuning of advanced boosting models.
* MLflow experiment tracking.
* Best-model selection using evaluation metrics.
* Model persistence using `.pkl` files.
* Streamlit-based prediction application.
* Docker containerization.
* Reproducible local deployment workflow.

---

## 👨‍💻 Author

**Akhlaque Alam**

**Aspiring Data Scientist | Machine Learning | Python | SQL | Streamlit | MLflow | Docker**
