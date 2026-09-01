
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



