import pandas as pd
import streamlit as st
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="Food Delivery Prediction",
    page_icon="🍔",
    layout="wide"
)


# Load Model
model = joblib.load("Food_Delivery_LightGBM_Tuned.pkl")
feature_columns = joblib.load("feature_columns.pkl")
freq_mappings = joblib.load("freq_mappings.pkl")


# Side bar inputs
st.sidebar.header("Delivery Details")

delivery_person_id = st.sidebar.selectbox(
    "Delivery Person ID",
    options=sorted(freq_mappings["Delivery_person_ID"].keys())
)

delivery_person_age = st.sidebar.slider(
    "Delivery Person Age",
    min_value=15.0,
    max_value=47.5,
    value=29.5818,
    step=0.1
)

delivery_person_ratings = st.sidebar.slider(
    "Delivery Person Ratings",
    min_value=4.3,
    max_value=5.1,
    value=4.6,
    step=0.1
)

restaurant_latitude = st.sidebar.number_input(
    "Restaurant Latitude",
    min_value=-1.7590345,
    max_value=30.914057,
    value=18.546947,
    step=0.0001
)

restaurant_longitude = st.sidebar.number_input(
    "Restaurant Longitude",
    min_value=65.8588575,
    max_value=85.35523749,
    value=75.952494,
    step=0.0001
)

delivery_location_latitude=st.sidebar.number_input(
    "Delivery Location Latitude",
    min_value=0.01,
    max_value=31.054057,
    value=18.633934,
    step=0.0001
)

delivery_location_longitude = st.sidebar.number_input(
    "Delivery Location Longitude",
    min_value=66.039434,
    max_value=85.34761,
    value=76.063,
    step=0.0001
)

vehicle_condition = st.sidebar.selectbox(
    "Vehicle Condition",
    options=[0, 1, 2, 3],
    index=1
)

multiple_deliveries = st.sidebar.slider(
    "Multiple Deliveries",
    min_value=0.0,
    max_value=2.5,
    value=0.7462659, 
    step=0.01
)

order_day = st.sidebar.slider(
    "Order Day",
    min_value=1,
    max_value=31,
    value=14,
    step=1,
)

order_month = st.sidebar.selectbox(
    "Order Month",
    options=[2, 3, 4],
    index=1
)

order_day_of_week = st.sidebar.selectbox(
    "Order Day of Week",
    options=[
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ],
    index=0
)

order_hour = st.sidebar.selectbox(
    "Order Hour",
    options=[0, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    index=11
)

order_minute = st.sidebar.selectbox(
    "Order Minute",
    options=[0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    index=3
)

pickup_hour = st.sidebar.selectbox(
    "Pickup Hour",
    options=[0, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    index=11
)

pickup_minute = st.sidebar.selectbox(
    "Pickup Minute",
    options=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    index=6
)

weather_conditions = st.sidebar.selectbox(
    "Weather Conditions",
    options=["Fog", "NaN", "Sandstorms", "Stormy", "Sunny", "Windy"],
    index=4
)

road_traffic_density = st.sidebar.selectbox(
    "Road Traffic Density",
    options=["Jam", "Low", "Medium"],
    index=1
)

type_of_order = st.sidebar.selectbox(
    "Type of Order",
    options=["Drinks", "Meal", "Snack"],
    index=0
)

type_of_vehicle = st.sidebar.selectbox(
    "Type of Vehicle",
    options=["Electric Scooter", "Motorcycle", "Scooter"],
    index=1
)

festival = st.sidebar.selectbox(
    "Festival",
    options=["Yes", "No"],
    index=0
)

city = st.sidebar.selectbox(
    "City",
    options=["Semi Urban", "Urban"],
    index=1
)



# DEFAULT VALUE
prediction = None

# Prediction Button
predict_button = st.sidebar.button("Predict Delivery")

order_day_of_week = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}[order_day_of_week]

if predict_button:

    delivery_person_id = freq_mappings["Delivery_person_ID"].get(delivery_person_id, 0)

    input_data = {
    "Delivery_person_ID": delivery_person_id,
    "Delivery_person_Age": delivery_person_age,
    "Delivery_person_Ratings": delivery_person_ratings,
    "Restaurant_latitude": restaurant_latitude,
    "Restaurant_longitude": restaurant_longitude,
    "Delivery_location_latitude": delivery_location_latitude,
    "Delivery_location_longitude": delivery_location_longitude,
    "Vehicle_condition": vehicle_condition,
    "multiple_deliveries": multiple_deliveries,
    "Order_Day": order_day,
    "Order_Month": order_month,
    "Order_Day_of_Week": order_day_of_week,
    "Order_Hour": order_hour,
    "Order_Minute": order_minute,
    "Pickup_Hour": pickup_hour,
    "Pickup_Minute": pickup_minute,

    "Weatherconditions_conditions Fog": 1 if weather_conditions == "Fog" else 0,
    "Weatherconditions_conditions NaN": 1 if weather_conditions == "NaN" else 0,
    "Weatherconditions_conditions Sandstorms": 1 if weather_conditions == "Sandstorms" else 0,
    "Weatherconditions_conditions Stormy": 1 if weather_conditions == "Stormy" else 0,
    "Weatherconditions_conditions Sunny": 1 if weather_conditions == "Sunny" else 0,
    "Weatherconditions_conditions Windy": 1 if weather_conditions == "Windy" else 0,

    "Road_traffic_density_Jam ": 1 if road_traffic_density == "Jam" else 0,
    "Road_traffic_density_Low ": 1 if road_traffic_density == "Low" else 0,
    "Road_traffic_density_Medium ": 1 if road_traffic_density == "Medium" else 0,

    "Type_of_order_Drinks ": 1 if type_of_order == "Drinks" else 0,
    "Type_of_order_Meal ": 1 if type_of_order == "Meal" else 0,
    "Type_of_order_Snack ": 1 if type_of_order == "Snack" else 0,

    "Type_of_vehicle_electric_scooter ": 1 if type_of_vehicle == "Electric Scooter" else 0,
    "Type_of_vehicle_motorcycle ": 1 if type_of_vehicle == "Motorcycle" else 0,
    "Type_of_vehicle_scooter ": 1 if type_of_vehicle == "Scooter" else 0,

    "Festival_Yes ": 1 if festival == "Yes" else 0,

    "City_Semi-Urban ": 1 if city == "Semi Urban" else 0,
    "City_Urban ": 1 if city == "Urban" else 0
}


    input_df = pd.DataFrame([input_data])

    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)[0]


# Header
st.title("🍔 Food Delivery Time Prediction")

st.caption(
    "An end-to-end machine learning application for predicting estimated food delivery time"
)


# TOP SECTION

left, right = st.columns([1.2, 1])

with left:

    st.subheader("Prediction")

    if prediction is not None:

        st.success(f"Estimated Delivery Time: {prediction:.0f} minutes")
        st.warning("Model Used : LightGBM Regressor")
    else:
        st.info(
            "This is an estimated delivery time based on the details provided."
        )

with right:

    st.subheader("Deployed Model")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Best Model",
            "LGBMR (Tuned)"
        )

    with col2:
        st.metric(
            "R² Score",
            "0.7935"
        )

    with col3:
        st.metric(
            "RMSE",
            "4.2554"
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "MAE",
            "3.3995"
        )

    with col5:
        st.metric(
            "MSE",
            "18.1084"
        )

    with col6:
        st.metric(
            "Model Type",
            "Regression"
        )


st.divider()





# Selected Food Delivery Scenario
st.subheader("Selected Food Delivery Scenario")

scenario_df = pd.DataFrame({
    "Features": [
        "Delivery Person ID",
        "Delivery Person Age",
        "Delivery Person Rating",
        "Restaurant Latitude",
        "Restaurant Longitude",
        "Delivery Location Latitude",
        "Delivery Location Longitude",
        "Vehicle Condition",
        "Multiple Deliveries",
        "Order Day",
        "Order Month",
        "Order Day of Week",
        "Order Hour",
        "Order Minute",
        "Pickup Hour",
        "Pickup Minute",
        "Weather Conditions",
        "Road Traffic Density",
        "Type of Order",
        "Type of Vehicle",
        "Festival",
        "City"
    ],
    "Selected Values": [
        delivery_person_id,
        delivery_person_age,
        delivery_person_ratings,
        restaurant_latitude,
        restaurant_longitude,
        delivery_location_latitude,
        delivery_location_longitude,
        vehicle_condition,
        multiple_deliveries,
        order_day,
        order_month,
        order_day_of_week,
        order_hour,
        order_minute,
        pickup_hour,
        pickup_minute,
        weather_conditions,
        road_traffic_density,
        type_of_order,
        type_of_vehicle,
        festival,
        city
    ]
})

st.dataframe(
    scenario_df,
    use_container_width=True
)



# Model Comparison Before Hyperparameter Tuning
comparison_df = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "KNN Regressor",
        "SVM Regressor",
        "DecisionTree Regressor",
        "RandomForest Regressor",
        "GradientBoosting Regressor",
        "XGBoost Regressor",
        "LightGBM Regressor",
        "CatBoost Regressor"
    ],
    "MAE": [
        4.993,
        5.576,
        5.571,
        4.901,
        3.745,
        4.074,
        3.515,
        3.576,
        3.480
    ],
    "MSE": [
        40.017,
        50.265,
        50.404,
        43.285,
        23.198,
        26.522,
        19.517,
        20.197,
        19.091
    ],
    "RMSE": [
        6.326,
        7.090,
        7.100,
        6.579,
        4.816,
        5.150,
        4.418,
        4.494,
        4.369
    ],
    "R2_Score": [
        0.544,
        0.427,
        0.425,
        0.506,
        0.735,
        0.698,
        0.777,
        0.770,
        0.782
    ]
})

st.subheader("Baseline Model Comparison")

st.dataframe(
    comparison_df.sort_values(
        by="R2_Score",
        ascending=False
    ),
    use_container_width=True
)


# Baseline Model Performance Visualization
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))

# Professional deployment colors
colors = [
    "#00B894" if model == "CatBoost" else "#6C8EBF"
    for model in comparison_df["Model"]
]

bars = ax.bar(
    comparison_df["Model"],
    comparison_df["R2_Score"],
    color=colors,
    width=0.65,
    edgecolor="black",
    linewidth=1
)

# Title
ax.set_title(
    "Baseline Model Comparison",
    fontsize=20,
    fontweight="bold",
    color="#1D3557",
    pad=22
)

# Axis labels
ax.set_xlabel(
    "Machine Learning Models",
    fontsize=12,
    fontweight="bold",
    labelpad=10
)

ax.set_ylabel(
    "R² Score",
    fontsize=12,
    fontweight="bold",
    labelpad=10
)

# Light horizontal grid
ax.grid(
    axis="y",
    linestyle="--",
    linewidth=0.7,
    alpha=0.20
)

ax.set_axisbelow(True)

# X-axis
ax.set_xticks(range(len(comparison_df)))
ax.set_xticklabels(
    comparison_df["Model"],
    rotation=30,
    ha="right",
    fontsize=10
)

# Y-axis
ax.tick_params(
    axis="y",
    labelsize=10
)

# Clean borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Value labels
for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.008,
        f"{height:.3f}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

# Highlight best model
best_index = comparison_df["R2_Score"].idxmax()

ax.text(
    best_index,
    comparison_df.loc[best_index, "R2_Score"] + 0.045,
    "★ Best Baseline",
    ha="center",
    fontsize=10,
    fontweight="bold",
    color="#00B894"
)

ax.set_ylim(0, 0.85)

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)



# Model Performance After Hyperparameter Tuning
tuning_comparison_df = pd.DataFrame({
    "Model": [
        "LightGBM Tuned",
        "XGBoost Tuned",
        "CatBoost Tuned",
        "CatBoost",
        "XGBoost",
        "LightGBM"
    ],
    "MAE": [
        3.3995,
        3.4394,
        3.4520,
        3.4801,
        3.5153,
        3.5760
    ],
    "MSE": [
        18.1084,
        18.6834,
        18.9816,
        19.0910,
        19.5171,
        20.1971
    ],
    "RMSE": [
        4.2554,
        4.3224,
        4.3568,
        4.3693,
        4.4178,
        4.4941
    ],
    "R2 Score": [
        0.7935,
        0.7869,
        0.7835,
        0.7823,
        0.7774,
        0.7696
    ]
})


st.subheader("Model Performance After Hyperparameter Tuning")

st.dataframe(
    tuning_comparison_df.sort_values(
        by="R2 Score",
        ascending=False
    ),
    use_container_width=True
)


# Model Performance After Hyperparameter Tuning
import matplotlib.pyplot as plt

plt.figure(figsize=(13, 7))

# Colors
colors = ['#5B8DB8'] * len(tuning_comparison_df)

# Highlight best tuned model
best_index = tuning_comparison_df['R2 Score'].idxmax()
best_position = tuning_comparison_df.index.get_loc(best_index)
colors[best_position] = '#2A9D8F'

bars = plt.bar(
    tuning_comparison_df['Model'],
    tuning_comparison_df['R2 Score'],
    color=colors,
    edgecolor='black',
    linewidth=1.2
)

# Title
plt.title(
    "Model Performance After Hyperparameter Tuning",
    fontsize=20,
    fontweight='bold',
    color='#264653',
    pad=20
)

# Axis labels
plt.xlabel(
    "Machine Learning Models",
    fontsize=14,
    fontweight='bold',
    color='#264653'
)

plt.ylabel(
    "R² Score",
    fontsize=14,
    fontweight='bold',
    color='#264653'
)

# Grid
plt.grid(
    axis='y',
    linestyle='--',
    linewidth=0.8,
    alpha=0.25
)

# Ticks
plt.xticks(
    rotation=30,
    ha='right',
    fontsize=11,
    fontweight='bold'
)

plt.yticks(fontsize=11)

# Remove top/right border
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Value labels
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.006,
        f"{height:.3f}",
        ha='center',
        fontsize=10,
        fontweight='bold',
        color='#264653'
    )

plt.ylim(0, 0.85)

plt.tight_layout()

st.pyplot(plt)

plt.close()




# Feature Importance
feature_importance_df = pd.DataFrame({
    "Feature": [
        "Order_Day",
        "Delivery_location_latitude",
        "Delivery_person_ID",
        "Delivery_location_longitude",
        "Restaurant_longitude",
        "Delivery_person_Age",
        "Restaurant_latitude",
        "Order_Hour",
        "Delivery_person_Ratings",
        "Pickup_Hour"
    ],
    "Importance": [
        4617,
        3844,
        3652,
        3387,
        3381,
        3375,
        3258,
        2954,
        2515,
        2362
    ]
})

st.subheader("Feature Importance")

st.dataframe(
    feature_importance_df,
    use_container_width=True,
    hide_index=True
)


# Feature Importance Visualization

import matplotlib.pyplot as plt

plt.figure(figsize=(11, 7))

# Sort features by importance
feature_plot_df = feature_importance_df.sort_values(
    by="Importance",
    ascending=True
)

# Colors
colors = ['#7A9E9F'] * len(feature_plot_df)

# Highlight most important feature
colors[-1] = '#E76F51'

bars = plt.barh(
    feature_plot_df["Feature"],
    feature_plot_df["Importance"],
    color=colors,
    edgecolor="black",
    linewidth=1
)

# Title
plt.title(
    "Top 10 Feature Importance",
    fontsize=20,
    fontweight="bold",
    color="#264653",
    pad=18
)

# Axis labels
plt.xlabel(
    "Importance",
    fontsize=13,
    fontweight="bold",
    color="#264653"
)

plt.ylabel(
    "Features",
    fontsize=13,
    fontweight="bold",
    color="#264653"
)

# Grid
plt.grid(
    axis="x",
    linestyle="--",
    linewidth=0.7,
    alpha=0.25
)

plt.gca().set_axisbelow(True)

# Remove unnecessary borders
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Value labels
for bar in bars:
    width = bar.get_width()

    plt.text(
        width + 50,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.0f}",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#264653"
    )

plt.tight_layout()

st.pyplot(plt)

plt.close()