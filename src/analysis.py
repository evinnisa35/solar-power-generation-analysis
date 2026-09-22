
# ==========================================
# 1. IMPORT LIBRARIES
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# 2. LOAD DATA
# ==========================================

generation = pd.read_csv("data/Generation.csv")
weather = pd.read_csv("data/Weather.csv")

print(generation.head())
print(weather.head())
print("Generation shape:", generation.shape)
print("Weather shape:", weather.shape)
print(generation.columns)
print(weather.columns)
print(generation.dtypes)
print(weather.dtypes)

# ==========================================
# 3. DATA PREPROCESSING
# ==========================================

generation["DATE_TIME"] = pd.to_datetime(
    generation["DATE_TIME"],
    dayfirst=True
)

weather["DATE_TIME"] = pd.to_datetime(
    weather["DATE_TIME"]
)
print(generation["DATE_TIME"].dtype)
print(weather["DATE_TIME"].dtype)

# ==========================================
# 4. HOURLY POWER GENERATION ANALYSIS
# ==========================================

generation["HOUR"] = generation["DATE_TIME"].dt.hour
print(generation[["DATE_TIME", "HOUR"]].head(10))
print(generation["HOUR"].unique())
print(generation["HOUR"].value_counts().sort_index())
hourly_power = generation.groupby("HOUR")["AC_POWER"].mean()
print(hourly_power)

# ==========================================
# 4.1 HOURLY POWER GENERATION VISUALIZATION
# ==========================================

plt.plot(hourly_power.index, hourly_power)
plt.xlabel("Hour")
plt.ylabel("Average AC Power (W)")
plt.title("Average Solar Power Generation by Hour")
plt.savefig("figures/daily_generation_profile.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================================
# 5. MERGE GENERATION AND WEATHER DATA
# ==========================================

merged_data = pd.merge(
    generation,
    weather,
    on="DATE_TIME"
)
print(merged_data.head())
print(merged_data.shape)

plt.scatter(merged_data["IRRADIATION"], merged_data["AC_POWER"])
plt.savefig("figures/irradiation_vs_ac_power.png", dpi=300, bbox_inches="tight")
plt.show()
correlation = np.corrcoef(
    merged_data["IRRADIATION"],
    merged_data["AC_POWER"]
)

print(correlation)
correlation = np.corrcoef(
    merged_data["AMBIENT_TEMPERATURE"],
    merged_data["AC_POWER"]
)

print(correlation)
correlation = np.corrcoef(
    merged_data["MODULE_TEMPERATURE"],
    merged_data["AC_POWER"]
)

print(correlation)

# ==========================================
# 5.1 MERGED DATA VALIDATION
# ==========================================

print(merged_data.isnull().sum())
print(merged_data.describe())

# ==========================================
# 6. INVERTER PERFORMANCE ANALYSIS
# ==========================================

inverter_power = generation.groupby("SOURCE_KEY")["AC_POWER"].mean()
print(inverter_power)
plt.figure(figsize=(12, 6))

plt.bar(inverter_power.index, inverter_power)

plt.xlabel("Inverter")
plt.ylabel("Average AC Power")
plt.title("Average AC Power by Inverter")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/inverter_comparison.png", dpi=300, bbox_inches="tight")
plt.show()
 
# ==========================================
# 7.1 CORRELATION ANALYSIS
# ==========================================

correlation = np.corrcoef(
    merged_data["IRRADIATION"],
    merged_data["AC_POWER"]
)

print("Irradiation vs AC Power correlation:")
print(correlation)

# ==========================================
# 8. AMBIENT TEMPERATURE VS AC POWER
# ==========================================

plt.scatter(
    merged_data["AMBIENT_TEMPERATURE"],
    merged_data["AC_POWER"]
)

plt.xlabel("Ambient Temperature (°C)")
plt.ylabel("AC Power (W)")
plt.title("Ambient Temperature vs AC Power")
plt.savefig("figures/ambient_temperature_vs_ac_power.png", dpi=300, bbox_inches="tight")

plt.show()

# ==========================================
# 8.1 CORRELATION ANALYSIS
# ==========================================

correlation = np.corrcoef(
    merged_data["AMBIENT_TEMPERATURE"],
    merged_data["AC_POWER"]
)

print("Ambient Temperature vs AC Power correlation:")
print(correlation)

# ==========================================
# 9. MODULE TEMPERATURE VS AC POWER
# ==========================================

plt.scatter(
    merged_data["MODULE_TEMPERATURE"],
    merged_data["AC_POWER"]
)

plt.xlabel("Module Temperature (°C)")
plt.ylabel("AC Power (W)")
plt.title("Module Temperature vs AC Power")
plt.savefig("figures/module_temperature_vs_ac_power.png", dpi=300, bbox_inches="tight")

plt.show()

# ==========================================
# 9.1 CORRELATION ANALYSIS
# ==========================================

correlation = np.corrcoef(
    merged_data["MODULE_TEMPERATURE"],
    merged_data["AC_POWER"]
)

print("Module Temperature vs AC Power correlation:")
print(correlation)

# ==========================================
# STAGE 2 - ML PREDICTION
# ==========================================

import pandas as pd

# ==========================================
# 1. LOAD DATA
# ==========================================

generation = pd.read_csv("data/Generation.csv")
weather = pd.read_csv("data/Weather.csv")

print("Generation shape:", generation.shape)
print("Weather shape:", weather.shape)

# ==========================================
# 2. DATE_TIME CONVERSION
# ==========================================

generation["DATE_TIME"] = pd.to_datetime(
    generation["DATE_TIME"],
    format="%d-%m-%Y %H:%M"
)

weather["DATE_TIME"] = pd.to_datetime(
    weather["DATE_TIME"]
)

print("\nGeneration DATE_TIME type:")
print(generation["DATE_TIME"].dtype)

print("\nWeather DATE_TIME type:")
print(weather["DATE_TIME"].dtype)

# ==========================================
# 3. MERGE DATA
# ==========================================

data = pd.merge(
    generation,
    weather,
    on=["DATE_TIME", "PLANT_ID"],
    how="inner"
)

print("\nMerged data shape:")
print(data.shape)

print("\nMerged data columns:")
print(data.columns)

# ==========================================
# 4. CLEAN MERGED DATA
# ==========================================

data = data.drop(columns=["SOURCE_KEY_y"])

data = data.rename(columns={
    "SOURCE_KEY_x": "SOURCE_KEY"
})

print("\nData columns after cleaning:")
print(data.columns)

print("\nData shape:")
print(data.shape)

# ==========================================
# 5. FEATURE ENGINEERING
# ==========================================

data["MONTH"] = data["DATE_TIME"].dt.month
data["DAY_OF_YEAR"] = data["DATE_TIME"].dt.dayofyear
data["HOUR"] = data["DATE_TIME"].dt.hour

print("\nFeature engineered data:")
print(
    data[
        ["DATE_TIME", "MONTH", "DAY_OF_YEAR", "HOUR"]
    ].head(10)
)

# ==========================================
# 6. FEATURES (X) AND TARGET (y)
# ==========================================

features = [
    "AMBIENT_TEMPERATURE",
    "MODULE_TEMPERATURE",
    "IRRADIATION",
    "MONTH",
    "DAY_OF_YEAR",
    "HOUR"
]

X = data[features]
y = data["AC_POWER"]

print("\nX shape:", X.shape)
print("y shape:", y.shape)

# ==========================================
# 7. TRAIN - TEST SPLIT
# ==========================================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nX_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# ==========================================
# 8. LINEAR REGRESSION MODEL
# ==========================================

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("\nLinear Regression training completed.")

# ==========================================
# 9. LINEAR REGRESSION PREDICTION
# ==========================================

y_pred = model.predict(X_test)

print("\nFirst 10 Linear Regression predictions:")
print(y_pred[:10])

# ==========================================
# 10. LINEAR REGRESSION PERFORMANCE
# ==========================================

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nLinear Regression Performance:")
print("MAE :", mae)
print("RMSE:", rmse)
print("R²  :", r2)

# ==========================================
# 11. RANDOM FOREST REGRESSION
# ==========================================

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

print("\nRandom Forest training completed.")

# ==========================================
# 12. RANDOM FOREST PREDICTION
# ==========================================

y_pred_rf = rf_model.predict(X_test)

print("\nFirst 10 Random Forest predictions:")
print(y_pred_rf[:10])

# ==========================================
# 13. RANDOM FOREST PERFORMANCE
# ==========================================

mae_rf = mean_absolute_error(y_test, y_pred_rf)
rmse_rf = mean_squared_error(y_test, y_pred_rf) ** 0.5
r2_rf = r2_score(y_test, y_pred_rf)

print("\nRandom Forest Performance:")
print("MAE :", mae_rf)
print("RMSE:", rmse_rf)
print("R²  :", r2_rf)

# ==========================================
# 14. MODEL COMPARISON
# ==========================================

print("\nModel Comparison:")
print("------------------------------------------")
print("Model              MAE       RMSE      R²")
print("------------------------------------------")
print(
    f"Linear Regression  {mae:.2f}     "
    f"{rmse:.2f}     {r2:.4f}"
)
print(
    f"Random Forest      {mae_rf:.2f}     "
    f"{rmse_rf:.2f}     {r2_rf:.4f}"
)
print("------------------------------------------")

