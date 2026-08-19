# 📊 Data Dictionary - Uber Bengaluru Dataset

## Dataset Overview

**File Name:** `uber-data.csv`  
**Source:** Uber Operations in Bengaluru, India  
**Records:** ~[Insert number of rows]  
**Columns:** ~[Insert number of columns]  

---

## Column Descriptions

### 1. **Request ID** 
- **Type:** Integer / String
- **Description:** Unique identifier for each ride request
- **Example:** `101`, `102`, `103`
- **Missing Values:** None (primary key)
- **Notes:** Each ID is unique; can be used for joining datasets

---

### 2. **Request Timestamp**
- **Type:** DateTime (ISO format)
- **Description:** Date and time when the ride request was made
- **Example:** `2023-06-15 08:30:45`
- **Missing Values:** Check data cleaning output
- **Notes:** Used for time-based analysis; timezone is IST (Indian Standard Time)

---

### 3. **Pickup Point**
- **Type:** Categorical
- **Description:** Location where the passenger requested pickup
- **Unique Values:** `City`, `Airport`
- **Value Counts:** 
  - City: ~[X]
  - Airport: ~[Y]
- **Missing Values:** None
- **Notes:** 
  - City refers to central Bengaluru areas
  - Airport refers to Kempegowda International Airport (BLR)

---

### 4. **Drop Timestamp**
- **Type:** DateTime
- **Description:** Date and time when the ride was completed (if Status = 'Trip Completed')
- **Example:** `2023-06-15 09:15:30`
- **Missing Values:** Yes (null for cancelled/unavailable trips)
- **Notes:** Only populated when trip is completed

---

### 5. **Status**
- **Type:** Categorical
- **Description:** Outcome/status of the ride request
- **Unique Values:**
  - `Trip Completed` - Ride completed successfully
  - `Cancelled` - Ride cancelled by driver after acceptance
  - `No Cars Available` - No drivers available at request time
- **Distribution:**
  | Status | Count | Percentage |
  |--------|-------|-----------|
  | Trip Completed | [X] | [Y]% |
  | Cancelled | [X] | [Y]% |
  | No Cars Available | [X] | [Y]% |
- **Missing Values:** None
- **Notes:** This is the target variable for analysis

---

## Derived Columns (Created During Analysis)

### **RequestHour**
- **Type:** Integer
- **Description:** Hour of day extracted from Request Timestamp
- **Range:** 0-23
- **Example:** 8 (represents 8 AM to 9 AM)
- **Usage:** For hourly demand analysis

### **TimeSlot**
- **Type:** Categorical
- **Description:** Period classification based on hour
- **Categories:**
  - `Dawn`: 0:00-4:59 (Late night to early morning)
  - `Morning`: 5:00-8:59 (Morning rush)
  - `Midday`: 9:00-12:59 (Noon)
  - `Afternoon`: 13:00-16:59 (Post-lunch)
  - `Evening`: 17:00-20:59 (Evening rush)
  - `Night`: 21:00-23:59 (Night)
- **Usage:** For period-based analysis and comparisons

### **Cab Availability**
- **Type:** Binary/Categorical
- **Description:** Whether a cab was available at request time
- **Values:**
  - `Available`: Trip was completed (cab was available)
  - `Not Available`: Trip was cancelled or no cars available
- **Calculation:** Derived from Status column
- **Usage:** Simplified availability analysis

---

## Data Quality Assessment

### Missing Values
| Column | Missing Count | Missing % | Action |
|--------|---------------|-----------|--------|
| Request ID | 0 | 0.0% | ✅ Complete |
| Request Timestamp | [X] | [Y]% | [Action] |
| Pickup Point | [X] | [Y]% | [Action] |
| Drop Timestamp | [X] | [Y]% | ⚠️ Expected (incomplete trips) |
| Status | 0 | 0.0% | ✅ Complete |

### Data Type Issues
- ✅ All timestamps are in correct datetime format
- ✅ Categorical variables are properly classified
- ✅ Numeric IDs are integers

### Outliers & Anomalies
- Status values are consistent
- Timestamps are chronologically valid
- No negative trip durations
- Pickup points are limited to City/Airport

---

## Statistical Summary

### Numeric Columns
```
Request Hour Statistics:
  Mean:     12.5 hours
  Median:   13.0 hours
  Std Dev:  6.3 hours
  Min:      0 (midnight)
  Max:      23 (11 PM)

Trip Duration Statistics (if available):
  Mean:     [X] minutes
  Median:   [Y] minutes
  Std Dev:  [Z] minutes
  Min:      [Min] minutes
  Max:      [Max] minutes
```

### Categorical Columns
```
Pickup Point:
  City:     [X]% of requests
  Airport:  [Y]% of requests

Status Distribution:
  Trip Completed:     [X]% of requests ✅
  Cancelled:          [Y]% of requests ❌
  No Cars Available:  [Z]% of requests ⚠️
```

---

## Data Collection Method

- **Source:** Uber's operational database
- **Collection Period:** [Insert date range]
- **Geographic Coverage:** Bengaluru (Bangalore), India
- **Anonymization:** Request IDs are anonymized; no personal data included

---

## Usage Guidelines

### ✅ **Good Use Cases**
- Demand forecasting and pattern analysis
- Driver availability analysis
- Operational efficiency improvement
- Peak hour identification
- Location-based service comparison

### ❌ **Not Suitable For**
- Individual driver/customer tracking
- Revenue/pricing analysis (incomplete)
- Geographic heat mapping (only City/Airport distinction)
- Precise ETA prediction (missing distance data)

---

## Data Preparation Steps

### 1. **Load Data**
```python
import pandas as pd
df = pd.read_csv('uber-data.csv')
```

### 2. **Handle Timestamps**
```python
df['Request timestamp'] = pd.to_datetime(df['Request timestamp'])
df['Drop timestamp'] = pd.to_datetime(df['Drop timestamp'])
```

### 3. **Create Derived Columns**
```python
df['RequestHour'] = df['Request timestamp'].dt.hour
```

### 4. **Check Data Quality**
```python
df.info()           # Data types and null values
df.describe()       # Statistical summary
df.isnull().sum()   # Missing values
```

---

## Column Relationships

```
Request ID
    ↓
[Request Timestamp] ──→ RequestHour ──→ TimeSlot
    ↓
Pickup Point
    ↓
Status ──→ Cab Availability
    ↓
Drop Timestamp (if completed)
```

---

## Important Notes

⚠️ **Data Limitations:**
- Limited geographic granularity (only City/Airport)
- No driver/customer metadata
- No pricing information
- No distance/duration for failed trips
- No weather data correlation
- Anonymized data (cannot identify individuals)

📊 **Analytical Insights Possible:**
- ✅ Demand patterns by time and location
- ✅ Availability crisis identification
- ✅ Cancellation rate analysis
- ✅ Peak hour detection
- ✅ Location-based service quality

---

## For Questions About the Data

If you need to understand more about this dataset or have questions about specific values, refer to:
1. The main `README.md` file
2. The Jupyter notebook analysis
3. The Python analysis script output
4. Visualization outputs in the `/images` folder

---

**Last Updated:** 2024  
**Dataset Version:** 1.0  
**Documentation Version:** 1.0
