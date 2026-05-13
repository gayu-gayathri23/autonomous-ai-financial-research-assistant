import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
stock = pd.read_csv('data/apple_stock.csv')

# Display first 5 rows
print("\nFIRST 5 ROWS")
print(stock.head())

# Dataset shape
print("\nDATASET SHAPE")
print(stock.shape)

# Column names
print("\nCOLUMN NAMES")
print(stock.columns)

# Missing values
print("\nMISSING VALUES")
print(stock.isnull().sum())

# Dataset information
print("\nDATASET INFO")
print(stock.info())

# Statistical summary
print("\nSTATISTICAL SUMMARY")
print(stock.describe())

# Plot closing price
plt.figure(figsize=(12,6))

stock['Close'] = pd.to_numeric(stock['Close'], errors='coerce')

plt.plot(stock['Close'])

plt.title('Apple Stock Closing Price')

plt.xlabel('Days')

plt.ylabel('Closing Price')

plt.show()