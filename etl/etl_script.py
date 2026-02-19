import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
df=pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\warehouse_inventory_project\data\processed\clean_inventory_data.csv")

#converting into date
df['last_restock_date']=pd.to_datetime(df['last_restock_date'])

#remove duplicates
df=df.drop_duplicates()

#remove missing values
df=df.dropna()

df.to_csv(r"C:\Users\hp\OneDrive\Desktop\warehouse_inventory_project\data\raw\raw_inventory_data.csv",index=False)


username = "root"
password = quote_plus("Shradha@2727")   
host = "127.0.0.1"
database = "ecommerce_dw"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@127.0.0.1:3306/{database}"
)


df.to_sql("inventory_raw", engine, if_exists="replace", index=False)

print("Connection Successful")

