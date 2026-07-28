# 🍔 Food Delivery Time Prediction

### End-to-End Machine Learning Regression Project

Predict food delivery time in minutes using delivery-partner, location, weather, traffic, vehicle, order, festival, and time-related features.

**Python · Machine Learning · LightGBM · MLflow · Streamlit · Docker**

---

## 🚀 Live Demo

**[🍔 Open Food Delivery Time Prediction App](https://akhlaque03-food-delivery-time-prediction.streamlit.app/)**

Enter delivery-related information and get an estimated delivery time directly from the trained Machine Learning model.

---

## 📌 Project Overview

**Food Delivery Time Prediction** is an end-to-end Machine Learning regression project that predicts the time required to deliver a food order in minutes.

The project uses delivery-partner information, restaurant and customer locations, weather, traffic, vehicle condition, order details, festival status, and time-related features to estimate delivery time.

The complete workflow covers:

**Data Cleaning → EDA → Feature Engineering → Model Training → MLflow Tracking → Hyperparameter Tuning → Best Model Selection → Model Registry → Model Persistence → Streamlit → Docker → Cloud Deployment**

---

## 🎯 Problem Statement

Food delivery time depends on multiple real-world factors such as traffic conditions, weather, delivery-partner ratings, vehicle condition, order details, location, festivals, and order timing.

Accurately estimating delivery time can help food-delivery platforms improve:

* Customer experience
* Delivery-time estimation
* Operational efficiency
* Delivery-partner allocation
* Logistics planning

This project uses historical delivery data to build a regression model capable of predicting expected food delivery time in minutes.

---

## 🎯 Project Objectives

* Build an end-to-end Machine Learning regression pipeline.
* Clean and preprocess real-world delivery data.
* Perform Exploratory Data Analysis (EDA).
* Engineer meaningful date and time features.
* Encode categorical variables and scale numerical features.
* Train and compare multiple regression algorithms.
* Track experiments and evaluation metrics using MLflow.
* Perform hyperparameter tuning on advanced boosting models.
* Select and register the best-performing model.
* Save the trained model and preprocessing artifacts.
* Build an interactive Streamlit prediction application.
* Containerize the application using Docker.
* Deploy the application to the cloud for live predictions.

---

## 🔄 Machine Learning Workflow

The project follows a complete end-to-end Machine Learning pipeline:

**Dataset → Data Cleaning → EDA → Feature Engineering → Model Training → MLflow Tracking → Hyperparameter Tuning → Best Model Selection → Model Registry → Model Persistence → Streamlit → Docker → Cloud Deployment**

### Workflow Stages

| Stage                 | What Was Done                                                        |
| --------------------- | -------------------------------------------------------------------- |
| Data Cleaning         | Handled missing values, invalid entries, data types, and outliers    |
| EDA                   | Analyzed target distribution, categorical features, and correlations |
| Feature Engineering   | Created date and time-based features                                 |
| Preprocessing         | Applied frequency encoding, one-hot encoding, and feature scaling    |
| Model Training        | Trained and compared multiple regression algorithms                  |
| MLflow Tracking       | Logged experiments and evaluation metrics                            |
| Hyperparameter Tuning | Optimized XGBoost, LightGBM, and CatBoost                            |
| Model Selection       | Selected the best-performing tuned model                             |
| Model Registry        | Registered the selected model                                        |
| Model Persistence     | Saved the trained model and preprocessing artifacts                  |
| Streamlit             | Built an interactive prediction application                          |
| Docker                | Containerized the application                                        |
| Cloud Deployment      | Deployed the application for live predictions                        |

---

## 📊 Dataset

The dataset contains historical food-delivery orders along with delivery-partner, location, weather, traffic, vehicle, order, festival, and time-related information.

### Target Variable

**`Time_taken(min)` — Food delivery time in minutes**

### Key Features

| Feature                       | Description                   |
| ----------------------------- | ----------------------------- |
| `Delivery_person_ID`          | Delivery partner identifier   |
| `Delivery_person_Age`         | Age of delivery partner       |
| `Delivery_person_Ratings`     | Delivery partner rating       |
| `Restaurant_latitude`         | Restaurant location latitude  |
| `Restaurant_longitude`        | Restaurant location longitude |
| `Delivery_location_latitude`  | Customer location latitude    |
| `Delivery_location_longitude` | Customer location longitude   |
| `Order_Date`                  | Order date                    |
| `Time_Orderd`                 | Order placement time          |
| `Time_Order_picked`           | Order pickup time             |
| `Weatherconditions`           | Weather condition             |
| `Road_traffic_density`        | Road traffic condition        |
| `Vehicle_condition`           | Vehicle condition             |
| `Type_of_order`               | Type of food order            |
| `Type_of_vehicle`             | Delivery vehicle type         |
| `multiple_deliveries`         | Number of deliveries handled  |
| `Festival`                    | Festival indicator            |
| `City`                        | Delivery city                 |

### Dataset Characteristics

* **45,593 delivery records**
* Numerical and categorical features
* Delivery-partner, location, weather, traffic, vehicle, order, and time-related information
* Real-world missing and inconsistent values
* Regression target measured in minutes

---

## 🧹 Data Cleaning & Preprocessing

The raw dataset contained missing values, inconsistent string entries, mixed data types, and extreme values. A structured preprocessing pipeline was applied before model training.

### Data Cleaning

* Removed the unnecessary `ID` column.
* Replaced invalid values such as `NaN ` with actual missing values.
* Converted numerical columns to appropriate numeric data types.
* Converted `Order_Date` into datetime format.
* Converted order and pickup time columns into usable datetime features.
* Removed original date and time columns after feature extraction.

### Missing Value Treatment

* Numerical missing values were replaced using **median imputation**.
* Categorical missing values were replaced using **mode imputation**.

### Outlier Treatment

Extreme numerical values were handled using **IQR-based clipping** to reduce the impact of unusually large or small observations while retaining the original records.

### Preprocessing Pipeline

* Frequency encoding for `Delivery_person_ID`
* One-hot encoding for relevant categorical variables
* Feature scaling for numerical features
* Train-test split before model training

The preprocessing approach ensures that the same feature transformations can be reproduced during model inference.

---

## ⚙️ Feature Engineering

Feature engineering was performed to extract meaningful information from date, time, and categorical variables.

### Date-Based Features

* `Order_Day`
* `Order_Month`
* `Order_Day_of_Week`

### Time-Based Features

* `Order_Hour`
* `Order_Minute`
* `Pickup_Hour`
* `Pickup_Minute`

### Categorical Encoding

Different encoding strategies were used based on the nature of each feature:

* **Frequency Encoding** → `Delivery_person_ID`
* **One-Hot Encoding** → Weather, traffic, order type, vehicle type, festival, and other categorical features

### Feature Scaling

Numerical features were scaled after encoding to ensure that features were represented on comparable scales for algorithms that are sensitive to feature magnitude.

---

## 🤖 Machine Learning Models

Multiple regression algorithms were trained and evaluated to identify the most suitable approach for food delivery time prediction.

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

### Hyperparameter Tuning

After baseline comparison, hyperparameter tuning was performed on:

* XGBoost
* LightGBM
* CatBoost

The tuned models were compared using the same evaluation metrics to select the final deployment model.

---

## 📈 Model Evaluation

The regression models were evaluated using four standard metrics:

* **R² Score** — Measures how well the model explains variance in delivery time.
* **MAE** — Measures average absolute prediction error in minutes.
* **MSE** — Measures average squared prediction error.
* **RMSE** — Measures prediction error in the same unit as the target variable.

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

> **Note:** These results represent the baseline model comparison before hyperparameter tuning. The final deployment model was selected after comparing the tuned candidates.

---

## 🏆 Hyperparameter Tuning & Final Model

After baseline model comparison, hyperparameter tuning was performed on:

* XGBoost
* LightGBM
* CatBoost

The tuned models were evaluated using **R² Score, MAE, MSE, and RMSE**.

### Final Model

**LightGBM Tuned** was selected as the final deployment model based on the tuned-model comparison.

The final trained model is saved as:

```text
Food_Deliver_lightgbm.pkl
```

### Why LightGBM?

LightGBM was selected for the final deployment workflow because it provided strong predictive performance while maintaining efficient training and inference.

---

## 📊 MLflow Experiment Tracking

[MLflow](https://mlflow.org/) was used to track and compare Machine Learning experiments throughout the project.

The experiment tracking workflow records:

* Model runs
* Model parameters
* Evaluation metrics
* Baseline model results
* Tuned model experiments
* Final model performance

### MLflow Experiment

```text
Food_Delivery_Prediction
```

MLflow helped maintain a structured record of model experiments and made it easier to compare different approaches before selecting the final deployment model.

### MLflow Tracking Screenshot

![MLflow Experiment Tracking](screenshorts/mlflow_experiment_tracking.png)

> `mlflow.db` is used as the local MLflow database backend and is kept out of version control.

---

## 🧠 Model & Preprocessing Artifacts

The trained model and preprocessing information are stored separately so the same transformations used during training can be reproduced during prediction.

| File                        | Purpose                                                       |
| --------------------------- | ------------------------------------------------------------- |
| `Food_Deliver_lightgbm.pkl` | Final trained LightGBM regression model                       |
| `feature_columns.pkl`       | Stores the feature-column structure required during inference |
| `freq_mappings.pkl`         | Stores frequency-encoding mappings used during preprocessing  |

These artifacts are loaded by the Streamlit application to prepare user inputs and generate predictions using the trained model.

---

## 🌐 Streamlit Application

The final trained LightGBM model was integrated into an interactive **Streamlit** web application.

Users can enter delivery-related information through the application, and the model generates an estimated **food delivery time in minutes**.

### Application Features

* Interactive input form
* Delivery-partner information
* Restaurant and delivery location details
* Weather and traffic conditions
* Vehicle and order information
* Festival and city information
* Real-time delivery-time prediction

### 🏠 Application Home Page

![Streamlit Home Page](screenshorts/home_page.png)

### 🎯 Prediction Result

![Prediction Result](screenshorts/prediction_result.png)

### 🚀 Live Application

**[Open Live Food Delivery Time Prediction App](https://akhlaque03-food-delivery-time-prediction.streamlit.app/)**

---

## 🐳 Docker Deployment

The application is containerized using Docker to provide a consistent and reproducible deployment environment.

The project includes a `Dockerfile` configured to run the Streamlit application.

### Build and Run

```bash
docker build -t food-delivery-app .
docker run -p 8501:8501 food-delivery-app
```

### Docker Container Screenshot

![Docker Container](screenshorts/docker_container_running.png)

---

## 🖥️ Local Setup & Installation

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Food-Delivery-Time-Prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
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

### Application & Deployment

* Streamlit
* Docker

### Development Environment

* Jupyter Notebook
* VS Code

---

## 📸 Project Screenshots

### Baseline Model Comparison

![Baseline Model Comparison](screenshorts/baseline_model_comparison.png)

### Baseline Model Graph

![Baseline Model Graph](screenshorts/baseline_model_graph.png)

### Tuned Model Comparison

![Tuned Model Comparison](screenshorts/tuned_model_comparison.png)

### Tuned Model Graph

![Tuned Model Graph](screenshorts/tuned_model_graph.png)

### Streamlit Home Page

![Streamlit Home Page](screenshorts/home_page.png)

### Prediction Result

![Prediction Result](screenshorts/prediction_result.png)

### MLflow Experiment Tracking

![MLflow Experiment Tracking](screenshorts/mlflow_experiment_tracking.png)

### LightGBM Tuned Metrics

![LightGBM Tuned Metrics](screenshorts/lightgbm_tuned_metrics.png)

### Docker Container

![Docker Container](screenshorts/docker_container_running.png)

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

The project successfully completed the Machine Learning lifecycle from data preprocessing to cloud deployment.

### Baseline Performance

The strongest baseline performance was achieved by **CatBoost**:

| Metric   |              Score |
| -------- | -----------------: |
| R² Score |         **0.7823** |
| MAE      | **3.4801 minutes** |
| RMSE     | **4.3693 minutes** |

The final deployment model was selected after **hyperparameter tuning and tuned-model comparison**.

### Deployment

* Model integrated with Streamlit.
* Application containerized using Docker.
* Application deployed to Streamlit Community Cloud.
* Live prediction interface available online.

### Live Application

**[🍔 Open Food Delivery Time Prediction App](https://akhlaque03-food-delivery-time-prediction.streamlit.app/)**

---

## 🚀 Future Improvements

The project can be further enhanced by:

* Adding real-time traffic and weather data through external APIs.
* Improving location-based features using geospatial distance calculations.
* Exploring advanced ensemble and deep-learning approaches.
* Adding automated model retraining pipelines.
* Implementing continuous MLflow model monitoring.
* Adding model explainability using SHAP.
* Deploying the application on AWS, Azure, or Google Cloud.
* Adding CI/CD automation for model and application deployment.
* Monitoring prediction performance after deployment.

---

## 👨‍💻 Author

### Akhlaque Alam

**Aspiring Data Scientist | Machine Learning | Python | SQL | Streamlit | MLflow | Docker**

Interested in building practical Machine Learning solutions and deploying data-driven applications.
