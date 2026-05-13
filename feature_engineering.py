import pandas as pd

# Load dataset
stock = pd.read_csv('data/apple_stock.csv')

# Fix column names
stock.columns = stock.columns.str.replace('AAPL', '')
stock.columns = stock.columns.str.replace('Ticker', '')
stock.columns = stock.columns.str.strip()

# Convert Close column to numeric
stock['Close'] = pd.to_numeric(stock['Close'], errors='coerce')

# Create Moving Averages
stock['MA_10'] = stock['Close'].rolling(10).mean()

stock['MA_50'] = stock['Close'].rolling(50).mean()

# Daily Return
stock['Daily_Return'] = stock['Close'].pct_change()

# Volatility
stock['Volatility'] = stock['Daily_Return'].rolling(10).std()

# Create Target Variable
stock['Target'] = (
    stock['Close'].shift(-1) > stock['Close']
).astype(int)

# Remove missing values
stock = stock.dropna()

# Save cleaned dataset
stock.to_csv(
    'data/featured_stock_data.csv',
    index=False
)

# Display output
print(stock.head())

print("\nFeature Engineering Completed Successfully!")