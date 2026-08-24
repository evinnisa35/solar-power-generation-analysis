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
