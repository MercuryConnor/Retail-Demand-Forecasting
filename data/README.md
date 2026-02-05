# Data Directory

This folder contains the raw datasets for the Retail Demand Forecasting pipeline.

## Required Data Files

The pipeline expects the following files:

```
data/
├── train.csv/
│   └── train.csv          (421,570 rows)
├── test.csv/
│   └── test.csv           (115,064 rows)
├── features.csv/
│   └── features.csv       (8,190 rows)
└── stores.csv             (45 rows)
```

## Data Sources

Download from Kaggle: [Walmart Recruiting - Store Sales Forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)

## Setup Instructions

1. Download the competition data from Kaggle
2. Extract files to this directory maintaining the structure above
3. Ensure CSV files are placed in their respective subdirectories

**Note**: Data files are not included in version control due to size (see `.gitignore`).
