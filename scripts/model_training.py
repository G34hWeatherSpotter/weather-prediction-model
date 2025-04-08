import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Step 1: Load the dataset with engineered features
data = pd.read_csv('data/featured_weather_data.csv', index_col='datetime', parse_dates=True)

# Step 2: Define features (X) and target (y)
X = data[['air_temp', 'windspeed', 'winddir', 'pressure', 'humidity', 'rainfall', 'fog', 'temp_rolling_mean', 'temp_diff']]
y = data['air_temp'].shift(-1).dropna()  # Predict the next time step's temperature

# Align features (X) with the shifted target (y)
X = X[:-1]

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Step 6: Save the trained model
joblib.dump(model, 'weather_model.pkl')
print("Model training complete! The model has been saved as 'weather_model.pkl'")
