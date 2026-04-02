from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://postgres:1234@localhost:5432/retail_db")

# Load datasets
train = pd.read_csv("data/train.csv/train.csv")
test = pd.read_csv("data/test.csv/test.csv")
features = pd.read_csv("data/features.csv/features.csv")
stores = pd.read_csv("data/stores.csv")

# Push to PostgreSQL
train.to_sql("train", engine, if_exists="replace", index=False)
test.to_sql("test", engine, if_exists="replace", index=False)
features.to_sql("features", engine, if_exists="replace", index=False)
stores.to_sql("stores", engine, if_exists="replace", index=False)

print("All tables loaded successfully.")