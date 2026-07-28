# Food Delivery Time Prediction

### End-to-End Machine Learning Regression Project

An end-to-end Machine Learning project that predicts food delivery time in minutes using delivery-partner information, geographical coordinates, weather, traffic, vehicle condition, order details, festival status, city, and time-based features.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-Tuned-9ACD32?style=for-the-badge)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?style=for-the-badge\&logo=mlflow\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)

</p>

---

## Project Highlights

* Real-world regression problem with **45,593 delivery records**
* Compared **9 regression algorithms**
* Performed hyperparameter tuning on **XGBoost, LightGBM, and CatBoost**
* Selected **LightGBM Tuned** as the final deployment model
* Achieved **R² = 0.7935**
* Used **MLflow** for experiment tracking and model management
* Built an interactive **Streamlit** prediction application
* Containerized the application using **Docker**
* Deployed the application to **Streamlit Community Cloud**

---

## Live Application

The trained model is available through an interactive Streamlit application.

**[Open Food Delivery Time Prediction App](https://akhlaque03-food-delivery-time-prediction.streamlit.app/)**

Users can enter delivery, location, weather, traffic, vehicle, order, and timing information to receive an estimated delivery time.

---

## Problem Statement

Food delivery time depends on multiple factors such as traffic conditions, weather, delivery-partner characteristics, vehicle condition, geographical location, order type, and time of day.

The objective of this project is to build a regression model that can estimate the expected delivery time in minutes from these real-world factors.

### Potential Business Value

A reliable delivery-time prediction system can support:

* More accurate customer delivery estimates
* Better delivery-partner allocation
* Operational planning
* Logistics optimization
* Improved customer experience

---

## Machine Learning Pipeline

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Data Preprocessing
     ↓
Train-Test Split
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
Model Registry
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

## Dataset

The dataset contains **45,593 historical food-delivery records** containing numerical, categorical, geographical, date, and time-related information.

### Target Variable

```text
Time_taken(min)
```

The target represents the total estimated food delivery time in minutes.

### Feature Categories

| Category         | Examples                            |
| ---------------- | ----------------------------------- |
| Delivery Partner | Age, Rating, ID                     |
| Location         | Restaurant and delivery coordinates |
| Timing           | Order date, order time, pickup time |
| Environment      | Weather conditions, road traffic    |
| Vehicle          | Vehicle type, vehicle condition     |
| Order            | Order type, multiple deliveries     |
| Context          | Festival, city                      |

### Important Features

```text
Delivery_person_ID
Delivery_person_Age
Delivery_person_Ratings
Restaurant_latitude
Restaurant_longitude
Delivery_location_latitude
Delivery_location_longitude
Vehicle_condition
multiple_deliveries
Weatherconditions
Road_traffic_density
Type_of_order
Type_of_vehicle
Festival
City
Order_Date
Time_Orderd
Time_Order_picked
```

---

## Data Cleaning & Preprocessing

The raw dataset contained inconsistent values, missing values, mixed data types, and extreme observations.

### Cleaning

* Removed the unnecessary `ID` column
* Converted invalid string values such as `NaN ` into missing values
* Converted numerical columns to appropriate numeric types
* Converted date columns into datetime format
* Extracted useful information from order and pickup times

### Missing Values

| Feature Type | Treatment |
| ------------ | --------- |
| Numerical    | Median    |
| Categorical  | Mode      |

### Outlier Treatment

IQR-based clipping was applied to selected numerical features to reduce the influence of extreme observations while retaining the original records.

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

### Scaling

Numerical features were scaled after encoding to ensure that scale-sensitive algorithms could work effectively.

---

## Feature Engineering

Date and time information was transformed into meaningful numerical features.

### Date Features

```text
Order_Day
Order_Month
Order_Day_of_Week
```

### Order Time Features

```text
Order_Hour
Order_Minute
```

### Pickup Time Features

```text
Pickup_Hour
Pickup_Minute
```

These features allow the model to capture temporal patterns related to delivery duration.

---

## Model Development

Nine regression algorithms were trained and evaluated:

1. Linear Regression
2. KNN Regressor
3. SVM Regressor
4. Decision Tree Regressor
5. Random Forest Regressor
6. Gradient Boosting Regressor
7. XGBoost Regressor
8. LightGBM Regressor
9. CatBoost Regressor

The baseline models were evaluated using:

* R² Score
* MAE
* MSE
* RMSE

---

## Baseline Model Performance

The baseline comparison showed that boosting algorithms performed particularly well on this dataset.

| Model             |       MAE |        MSE |      RMSE |  R² Score |
| ----------------- | --------: | ---------: | --------: | --------: |
| **CatBoost**      | **3.480** | **19.091** | **4.369** | **0.782** |
| XGBoost           |     3.515 |     19.517 |     4.418 |     0.777 |
| LightGBM          |     3.576 |     20.197 |     4.494 |     0.770 |
| Random Forest     |     3.745 |     23.198 |     4.816 |     0.735 |
| Gradient Boosting |     4.074 |     26.522 |     5.150 |     0.698 |
| Linear Regression |     4.993 |     40.017 |     6.326 |     0.544 |
| Decision Tree     |     4.901 |     43.285 |     6.579 |     0.506 |
| KNN Regressor     |     5.576 |     50.265 |     7.090 |     0.427 |
| SVM Regressor     |     5.571 |     50.404 |     7.100 |     0.425 |

### Baseline Model Comparison

![Baseline Model Comparison](screenshorts/baseline_model_comparison.png)

### Baseline Model Performance

![Baseline Model Graph](screenshorts/baseline_model_graph.png)

---

## Hyperparameter Tuning

After baseline comparison, the three strongest boosting candidates were selected for further optimization:

* XGBoost
* LightGBM
* CatBoost

`RandomizedSearchCV` with **5-fold cross-validation** was used for hyperparameter optimization.

### LightGBM Search Space

The tuning process explored parameters including:

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

The LightGBM tuning process used **40 randomized parameter combinations** with parallel processing.

---

## Tuned Model Comparison

After hyperparameter tuning, the models were compared using the same evaluation metrics.

| Model              |        MAE |         MSE |       RMSE |   R² Score |
| ------------------ | ---------: | ----------: | ---------: | ---------: |
| **LightGBM Tuned** | **3.3995** | **18.1084** | **4.2554** | **0.7935** |
| XGBoost Tuned      |     3.4394 |     18.6834 |     4.3224 |     0.7869 |
| CatBoost Tuned     |     3.4520 |     18.9816 |     4.3568 |     0.7835 |
| CatBoost           |     3.4801 |     19.0910 |     4.3693 |     0.7823 |
| XGBoost            |     3.5153 |     19.5171 |     4.4178 |     0.7774 |
| LightGBM           |     3.5760 |     20.1971 |     4.4941 |     0.7696 |

### Tuned Model Comparison

![Tuned Model Comparison](screenshorts/tuned_model_comparison.png)

### Tuned Model Performance

![Tuned Model Graph](screenshorts/tuned_model_graph.png)

---

## Final Model

### LightGBM Tuned

The final deployment model is **LightGBM Tuned**, selected based on the tuned-model comparison.

| Metric       |             Result |
| ------------ | -----------------: |
| **R² Score** |         **0.7935** |
| **MAE**      | **3.3995 minutes** |
| **RMSE**     | **4.2554 minutes** |
| **MSE**      |        **18.1084** |

Compared with the baseline LightGBM model:

```text
Baseline R²     = 0.7696
Tuned R²        = 0.7935

Baseline MAE    = 3.5760
Tuned MAE       = 3.3995

Baseline RMSE   = 4.4941
Tuned RMSE      = 4.2554
```

The tuned model improved both predictive performance and error metrics compared with the baseline LightGBM model.

### Final Model Artifact

```text
Food_Delivery_LightGBM_Tuned.pkl
```

---

## Feature Importance

The final model's most important features include geographical, delivery-partner, and time-related variables.

| Feature                     | Importance |
| --------------------------- | ---------: |
| Order_Day                   |       4617 |
| Delivery_location_latitude  |       3844 |
| Delivery_person_ID          |       3652 |
| Delivery_location_longitude |       3387 |
| Restaurant_longitude        |       3381 |
| Delivery_person_Age         |       3375 |
| Restaurant_latitude         |       3258 |
| Order_Hour                  |       2954 |
| Delivery_person_Ratings     |       2515 |
| Pickup_Hour                 |       2362 |

### Top Feature Importance

![Feature Importance](screenshorts/feature_importance.png)

---

## MLflow Experiment Tracking

MLflow was integrated into the project to track machine learning experiments and compare model performance systematically.

### Tracked Information

* Model parameters
* Training runs
* Evaluation metrics
* Baseline model experiments
* Hyperparameter tuning experiments
* Final model performance
* Model registration workflow

### Experiment

```text
Food_Delivery_Prediction
```

### MLflow Tracking

![MLflow Experiment Tracking](screenshorts/mlflow_experiment_tracking.png)

MLflow was used locally with a SQLite backend during development.

---

## Model Artifacts

The Streamlit application loads the trained model together with the preprocessing artifacts required for inference.

| Artifact                           | Purpose                                         |
| ---------------------------------- | ----------------------------------------------- |
| `Food_Delivery_LightGBM_Tuned.pkl` | Final trained LightGBM model                    |
| `feature_columns.pkl`              | Maintains the expected feature-column structure |
| `freq_mappings.pkl`                | Stores frequency-encoding mappings              |

This ensures that user inputs are transformed consistently with the data used during model training.

---

## Streamlit Application

The trained model was integrated into an interactive Streamlit application.

### Application Capabilities

* Delivery-partner information input
* Restaurant and customer location input
* Weather condition selection
* Traffic condition selection
* Vehicle information
* Order information
* Festival and city selection
* Order and pickup timing
* Estimated delivery-time prediction
* Model performance display
* Feature importance visualization
* Baseline and tuned model comparison

### Application Home Page

![Streamlit Home Page](screenshorts/home_page.png)

### Prediction Result

![Prediction Result](screenshorts/prediction_result.png)

---

## Docker

The application was containerized using Docker to provide a consistent environment for running the Streamlit application.

### Build Image

```bash
docker build -t food-delivery-time-prediction .
```

### Run Container

```bash
docker run -p 8501:8501 food-delivery-time-prediction
```

### Docker Application

![Docker Container Running](screenshorts/docker_container_running.png)

---

## Local Setup

### Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Food-Delivery-Time-Prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment on Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## Run MLflow Locally

To launch the MLflow tracking interface:

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

MLflow UI:

```text
http://127.0.0.1:5000
```

The local MLflow database is used for experiment tracking during development and should not be committed to the repository.

---

## Technology Stack

| Area                | Technologies                |
| ------------------- | --------------------------- |
| Language            | Python                      |
| Data Processing     | Pandas, NumPy               |
| Machine Learning    | Scikit-learn                |
| Boosting            | XGBoost, LightGBM, CatBoost |
| Visualization       | Matplotlib, Seaborn         |
| Experiment Tracking | MLflow                      |
| Web Application     | Streamlit                   |
| Containerization    | Docker                      |
| Deployment          | Streamlit Community Cloud   |
| Development         | Jupyter Notebook, VS Code   |

---

## Project Structure

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
    ├── feature_importance.png
    ├── home_page.png
    ├── lightgbm_tuned_metrics.png
    ├── mlflow_experiment_tracking.png
    ├── prediction_result.png
    ├── tuned_model_comparison.png
    └── tuned_model_graph.png
```

---

## Key Results

The project demonstrates the complete process of taking a real-world dataset from preprocessing and model development to experiment tracking and deployment.

### Model Performance

```text
Final Model        : LightGBM Tuned
R² Score           : 0.7935
MAE                : 3.3995 minutes
RMSE               : 4.2554 minutes
MSE                : 18.1084
```

### Deployment

```text
Model Training        ✓
Model Comparison      ✓
Hyperparameter Tuning ✓
MLflow Tracking       ✓
Model Registry        ✓
Model Persistence     ✓
Streamlit Application ✓
Docker Container      ✓
Cloud Deployment      ✓
```

---

## Future Improvements

Potential extensions for the project include:

* Real-time traffic API integration
* Real-time weather API integration
* Geospatial distance and route-based features
* SHAP-based model explainability
* Automated model retraining
* MLflow production monitoring
* CI/CD automation
* Cloud deployment using AWS, Azure, or Google Cloud
* Continuous model-performance monitoring

---

## Author

### Akhlaque Alam

**Aspiring Data Scientist | Machine Learning | Python | SQL | Streamlit | MLflow | Docker**

Focused on building practical Machine Learning solutions, developing predictive applications, and deploying data-driven projects from experimentation to production.

---
