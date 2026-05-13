import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

import joblib

# Load featured dataset
stock = pd.read_csv(
    'data/featured_stock_data.csv'
)

# Features
features = [
    'Close',
    'MA_10',
    'MA_50',
    'Daily_Return',
    'Volatility'
]

X = stock[features]

# Target variable
y = stock['Target']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nMODEL ACCURACY")
print(accuracy)

# Save model
joblib.dump(
    model,
    'models/stock_model.pkl'
)

print("\nModel saved successfully!")