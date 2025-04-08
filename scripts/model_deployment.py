import joblib
import pandas as pd
import numpy as np

# Load the model
model = joblib.load('weather_model.pkl')

# Define a function to preprocess new data and make predictions
def predict_weather(new_data):
    # Preprocess new data
    new_data['datetime'] = pd.to_datetime(new_data[['Year', 'Month', 'Day', 'Hour']])
    new_data = new_data.set_index('datetime')
    new_data = new_data.drop(columns=['Year', 'Month', 'Day', 'Hour', 'AOD'])
    
    # Feature Engineering
    new_data['temp_rolling_mean'] = new_data['air_temp'].rolling(window=3).mean()
    new_data['temp_diff'] = new_data['air_temp'].diff()
    new_data = new_data.dropna()
    
    # Prepare features
    X_new = new_data[['air_temp', 'windspeed', 'winddir', 'pressure', 'humidity', 'rainfall', 'fog', 'temp_rolling_mean', 'temp_diff']]
    
    # Make predictions
    predictions = model.predict(X_new)
    return predictions

# Example usage
new_data = pd.DataFrame({
    'Year': [2025, 2025, 2025],
    'Month': [4, 4, 4],
    'Day': [8, 8, 8],
    'Hour': [10, 11, 12],
    'air_temp': [20.0, 21.0, 22.0],
    'windspeed': [5.0, 5.0, 5.0],
    'winddir': [180, 180, 180],
    'pressure': [1010, 1011, 1012],
    'humidity': [60, 61, 62],
    'rainfall': [0, 0, 0],
    'fog': [0, 0, 0]
})

predictions = predict_weather(new_data)
print(predictions)
