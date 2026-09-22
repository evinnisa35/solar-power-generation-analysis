# Solar Power Generation Analysis

A data analysis and machine learning project focused on analyzing solar power generation data and predicting AC power output using environmental and time-based features.

The project is developed in multiple stages, starting with exploratory data analysis and continuing with machine learning-based power prediction.

---

## Project Overview

Solar power generation is affected by several factors, including solar irradiation, temperature, time of day, and seasonal changes.

In this project, solar power generation data and weather data are analyzed to:

* Explore solar power generation patterns
* Analyze the relationship between environmental conditions and AC power
* Compare inverter-level power generation
* Build machine learning models for AC power prediction
* Evaluate and compare different regression models

The project is organized into three stages:

* **Stage 1:** Data Analysis
* **Stage 2:** Machine Learning Prediction
* **Stage 3:** Advanced PV Analysis

---

## Dataset

The dataset used in this project is the **Solar Power Generation Data** dataset from Kaggle.

It contains two main datasets:

### Generation Data

The Generation dataset contains approximately 68,000 observations and includes:

* `DATE_TIME`
* `PLANT_ID`
* `SOURCE_KEY`
* `DC_POWER`
* `AC_POWER`
* `DAILY_YIELD`
* `TOTAL_YIELD`

### Weather Data

The Weather dataset contains environmental measurements including:

* `DATE_TIME`
* `PLANT_ID`
* `SOURCE_KEY`
* `AMBIENT_TEMPERATURE`
* `MODULE_TEMPERATURE`
* `IRRADIATION`

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* VS Code
* Git & GitHub

---

# Stage 1 - Data Analysis

## 1. Data Preprocessing

The first stage focuses on preparing and understanding the datasets.

The following operations were performed:

* Loading the Generation and Weather datasets
* Inspecting dataset dimensions and data types
* Converting timestamp columns into datetime format
* Extracting time-related information
* Merging Generation and Weather data
* Checking missing values
* Checking statistical distributions
* Investigating abnormal and zero-power observations

The two datasets were merged using `DATE_TIME` and `PLANT_ID`.

After merging, the resulting dataset contained:

* **68,774 observations**
* **13 variables**

No missing values were found in the merged dataset.

---

## 2. Daily Power Generation Profile

The daily generation profile was analyzed to observe how solar power production changes throughout the day.

The analysis shows the expected daily pattern of solar generation, with power production increasing after sunrise, reaching higher levels during daylight hours, and decreasing toward sunset.

---

## 3. Solar Irradiation vs AC Power

The relationship between solar irradiation and AC power was analyzed using correlation.

The Pearson correlation coefficient was:

**r = 0.989**

This indicates a very strong positive relationship between solar irradiation and AC power in this dataset.

---

## 4. Temperature Analysis

The relationship between temperature measurements and AC power was also investigated.

The observed correlations with AC power were approximately:

| Variable            | Correlation with AC Power |
| ------------------- | ------------------------: |
| Ambient Temperature |                      0.72 |
| Module Temperature  |                      0.95 |
| Solar Irradiation   |                     0.989 |

Solar irradiation showed the strongest relationship with AC power among these variables.

---

## 5. Inverter Analysis

Average AC power was compared between different inverter sources using the `SOURCE_KEY` variable.

This analysis was used to observe differences in power generation between inverter sources.

The differences were not directly interpreted as inverter efficiency because power output can also be affected by operating conditions and environmental factors.

---

# Stage 2 - Machine Learning Prediction

The second stage focuses on predicting AC power generation using machine learning.

## 1. Feature Engineering

Additional time-based features were extracted from the timestamp:

* `MONTH`
* `DAY_OF_YEAR`
* `HOUR`

These features were combined with environmental measurements to predict `AC_POWER`.

The input features used by the models were:

* `AMBIENT_TEMPERATURE`
* `MODULE_TEMPERATURE`
* `IRRADIATION`
* `MONTH`
* `DAY_OF_YEAR`
* `HOUR`

The target variable was:

* `AC_POWER`

---

## 2. Train-Test Split

The dataset was divided into training and testing sets.

* **80%** of the data was used for training
* **20%** was used for testing
* `random_state = 42`

The resulting dataset sizes were:

* Training set: **55,019 observations**
* Test set: **13,755 observations**

---

## 3. Linear Regression

A Linear Regression model was trained to predict AC power.

The model was evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² score

---

## 4. Random Forest Regression

A Random Forest Regression model was also trained.

The model was configured with:

* `n_estimators = 100`
* `random_state = 42`
* `n_jobs = -1`

Random Forest was evaluated using the same metrics as Linear Regression.

---

## 5. Model Evaluation

The two models were evaluated on the same test dataset.

| Model             |   MAE |  RMSE |     R² |
| ----------------- | ----: | ----: | -----: |
| Linear Regression | 26.33 | 55.36 | 0.9801 |
| Random Forest     | 16.37 | 45.67 | 0.9865 |

### Evaluation Metrics

**MAE (Mean Absolute Error)** measures the average absolute difference between actual and predicted values.

**RMSE (Root Mean Squared Error)** measures prediction error while giving greater weight to larger errors.

**R² (R-squared)** indicates how much of the variation in the target variable is explained by the model.

For this dataset and test split, Random Forest produced lower MAE and RMSE values and a higher R² value than Linear Regression.

---

# Stage 3 - Advanced PV Analysis

Stage 3 is planned as a future extension of the project.

Planned features include:

* Anomaly detection
* Inverter performance analysis
* Weather-based power analysis
* Real-time prediction
* Dashboard development
* Operational insights

---

## Project Structure

```text
solar-power-generation-analysis/
│
├── data/
│   ├── Generation.csv
│   └── Weather.csv
│
├── figures/
│   ├── daily_generation_profile.png
│   ├── irradiation_vs_ac_power.png
│   ├── module_temperature_vs_ac_power.png
│   ├── ambient_temperature_vs_ac_power.png
│   └── inverter_comparison.png
│
├── src/
│   └── analysis.py
│
├── README.md
└── requirements.txt
```

---

## Project Status

### Stage 1 - Data Analysis: Completed

* Data cleaning and preprocessing
* Exploratory data analysis
* Solar irradiation and AC power analysis
* Temperature analysis
* Inverter-level analysis

### Stage 2 - Machine Learning Prediction: Completed

* Feature engineering
* Train-test split
* Linear Regression
* Random Forest Regression
* AC power prediction
* Model evaluation using MAE, RMSE and R²
* Model comparison

### Stage 3 - Advanced PV Analysis: Planned

* Anomaly detection
* Inverter performance analysis
* Weather-based analysis
* Real-time prediction
* Dashboard
* Operational insights

```
Yani şu anda **sadece README'yi değiştirmen yeterli.** Sonra bana “yapıştırdım” de, `requirements.txt` ve GitHub kısmına geçelim.
```
