## 📊 Dataset

This project uses the following publicly available dataset from Kaggle:

**Solar Power Generation Data**  
Dataset by Anikannal

[View dataset on Kaggle](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data)

The dataset contains real-world measurements from a photovoltaic (PV) power plant.

### Generation Data

The generation dataset contains approximately **68,000 records** and includes:

- `DATE_TIME` - Measurement timestamp
- `PLANT_ID` - Solar power plant identifier
- `SOURCE_KEY` - Inverter identifier
- `DC_POWER` - DC-side power
- `AC_POWER` - AC-side power
- `DAILY_YIELD` - Daily energy yield
- `TOTAL_YIELD` - Total accumulated energy yield

### Weather Data

The weather dataset contains environmental measurements including:

- `DATE_TIME` - Measurement timestamp
- `PLANT_ID` - Solar power plant identifier
- `SOURCE_KEY` - Weather sensor identifier
- `AMBIENT_TEMPERATURE` - Ambient temperature
- `MODULE_TEMPERATURE` - PV module temperature
- `IRRADIATION` - Solar irradiation

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- VS Code
- Git & GitHub

---

##  Data Processing

The following preprocessing steps were performed:

1. Loaded the generation and weather datasets.
2. Inspected dataset dimensions and data types.
3. Converted timestamp columns to `datetime` format.
4. Extracted the hour from the timestamp.
5. Merged generation and weather data using `DATE_TIME`.
6. Checked for missing values.
7. Examined statistical distributions and possible abnormal values.

After merging, the main analysis dataset contained:

**68,774 observations and 13 variables.**

No missing values were detected in the merged dataset.

---

##  Analysis

### 1. Daily Power Generation Profile

Average AC power was calculated for each hour of the day.

The analysis shows the expected photovoltaic generation pattern:

- Near-zero generation during nighttime
- Increasing production during the morning
- Maximum production around midday
- Decreasing production during the afternoon
- Near-zero production after sunset

This confirms that the dataset reflects a realistic solar generation pattern.

---

### 2. Solar Irradiation vs AC Power

A scatter plot was used to investigate the relationship between solar irradiation
and AC power generation.

The calculated Pearson correlation coefficient was:

**r = 0.989**

This indicates a very strong positive linear relationship between solar
irradiation and AC power generation in this dataset.

> Correlation should not be interpreted as proof of causation. Other
> environmental and system variables can also influence PV generation.

---

### 3. Temperature Analysis

The relationship between AC power and temperature variables was also examined.

| Variable | Correlation with AC Power |
|---|---:|
| Ambient Temperature | 0.72 |
| Module Temperature | 0.95 |
| Solar Irradiation | 0.989 |

Solar irradiation showed the strongest correlation with AC power.

The high correlation between module temperature and AC power is also
consistent with the fact that module temperature is strongly affected by
solar irradiation.

---

### 4. Inverter Comparison

The dataset contains measurements from multiple inverters identified by
`SOURCE_KEY`.

Average AC power was calculated for each inverter to compare their
generation behavior.

The current analysis found differences between inverter-level average
power outputs.

These differences will be investigated further in later stages of the
project rather than being directly interpreted as differences in inverter
efficiency.

---

## 📁 Project Structure

```text
solar-power-generation-analysis/
│
├── data/
│   ├── generation.csv
│   └── weather.csv
│
├── notebooks/
│   └── solar_power_analysis.ipynb
│
├── figures/
│   ├── daily_generation_profile.png
│   ├── irradiation_vs_ac_power.png
│   └── inverter_comparison.png
│
├── src/
│   └── analysis.py
│
├── README.md
└── requirements.txt
 Future Work

This project is the first stage of a larger AI-integrated solar power
plant analysis system.

Planned future developments include:

Stage 2 - Machine Learning
Feature engineering
Solar power generation prediction
Train/test split
Regression models
Model evaluation using MAE, RMSE and R²
Comparison of different machine learning algorithms
Stage 3 - AI-Integrated Solar Plant Monitoring
Real-time generation prediction
Anomaly detection
Inverter performance monitoring
Weather-based generation forecasting
Interactive dashboard
AI-assisted operational insights

Author

Evin Nisa Terat

Electrical and Electronics Engineering Student


Project Status

Stage 1 - Data Analysis: Completed

Stage 2 - Machine Learning: Planned

Stage 3 - AI-Integrated Monitoring System: Planned

