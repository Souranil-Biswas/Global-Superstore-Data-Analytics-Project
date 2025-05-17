import pandas as pd
df = pd.read_csv(r"C:\Users\SOURANIL\Downloads\Global_Superstore2.csv" , encoding='latin1')

# dropping duplicates , null values & unimportant columns
df = df.drop_duplicates()
useless = ['Row ID','Order ID', 'Customer ID', 'Customer Name','Postal Code',  'Product ID', 'Product Name']

df= df.drop(columns= useless)
df = df.dropna()

#standardizing the whole data
df['Sales'] = df['Sales'].round(2)
df['Profit'] = df['Profit'].round(2)
df['Discount'] = df['Discount'].round(2)

df['Order Date'] = pd.to_datetime(df['Order Date'],errors='coerce',dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'],errors='coerce',dayfirst=True)

#calcuting outliuer values
q1_sales = df['Sales'].quantile(0.05)
q3_sales = df['Sales'].quantile(0.95)
IQR_sales = q3_sales - q1_sales

q1_Quantity = df['Quantity'].quantile(0.05)
q3_Quantity = df['Quantity'].quantile(0.95)
IQR_Quantity = q3_Quantity - q1_Quantity

q1_Profit = df['Profit'].quantile(0.05)
q3_Profit = df['Profit'].quantile(0.95)
IQR_Profit = q3_Profit - q1_Profit

q1_Discount = df['Discount'].quantile(0.05)
q3_Discount = df['Discount'].quantile(0.95)
IQR_Discount = q3_Discount - q1_Discount

lower_bound_sales = q1_sales - IQR_sales*1.5
upper_bound_sales = q3_sales + IQR_sales*1.5

lower_bound_quantity = q1_Quantity - IQR_Quantity*1.5
upper_bound_quantity = q3_Quantity + IQR_Quantity*1.5

lower_bound_profit = q1_Profit - IQR_Profit*1.5
upper_bound_profit = q3_Profit + IQR_Profit*1.5

lower_bound_discount = q1_Discount - IQR_Discount*1.5
upper_bound_discount = q3_Discount + IQR_Discount*1.5

clean = ((df['Sales']>= lower_bound_sales) & (df['Sales']<= upper_bound_sales) &
              (df['Quantity']>= lower_bound_quantity) & (df['Quantity']<= upper_bound_quantity) &
              (df['Profit']>= lower_bound_profit) & (df['Profit']<= upper_bound_profit) &
              (df['Discount']>= lower_bound_discount) & (df['Discount']<= upper_bound_discount))

df_cleaned = df[clean]

df_cleaned.to_csv(r"C:\Users\SOURANIL\Downloads\Cleaned Global SuperStore3.csv", index=False)
