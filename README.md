# Retail AI

End-to-end retail analytics and forecasting project demonstrating data engineering, data quality management, business KPI analysis, and machine learning foundations.

## Project Objectives

* Build a production-style retail analytics pipeline
* Perform data quality assessment and cleansing
* Generate business KPIs
* Create visual insights
* Prepare datasets for forecasting models

## Dataset

Online Retail Dataset

* Original records: 541,909
* Clean records: 392,692

## Data Quality Findings

| Metric               | Count   |
| -------------------- | ------- |
| Missing Customer IDs | 135,080 |
| Missing Descriptions | 1,454   |
| Duplicate Records    | 5,268   |
| Negative Quantities  | 10,624  |
| Negative Prices      | 2       |

## Business Insights

### Top Revenue Countries

1. United Kingdom
2. Netherlands
3. EIRE
4. Germany
5. France

### Top Revenue Products

1. PAPER CRAFT, LITTLE BIRDIE
2. REGENCY CAKESTAND 3 TIER
3. WHITE HANGING HEART T-LIGHT HOLDER

## Architecture

Raw Excel Data
→ Data Profiling
→ Data Quality Checks
→ Data Cleansing
→ KPI Analysis
→ Visualization
→ Forecasting (Next Phase)

## Technology Stack

* Python
* Pandas
* Matplotlib
* Scikit-learn
* Git
* GitHub
* Jupyter

## Project Status

Phase 1 Complete:

* Data ingestion
* Data quality analysis
* Data cleansing
* KPI generation
* Visualization

Next:

* Time-series forecasting
* Feature engineering
* Model evaluation
* CI/CD automation
## Visualizations

### Top Countries by Revenue

![Top Countries](docs/images/top_10_countries_revenue.png)

### Monthly Revenue Trend

![Revenue Trend](docs/images/monthly_revenue_trend.png)

### Revenue Forecast

![Revenue Forecast](docs/images/revenue_forecast.png)