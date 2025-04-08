import pandas as pd

# Load preprocessed data from the previous step
data = pd.read_csv('data/cleaned_weather_data.csv', index_col='datetime', parse_dates=True)

# Feature Engineering
# Create rolling averages for temperature
data['temp_rolling_mean'] = data['air_temp'].rolling(window=3).mean()

# Create temperature differences
data['temp_diff'] = data['air_temp'].diff()

# Drop rows with NaN values created by rolling mean and diff
data = data.dropna()

# Save the data with the new features
data.to_csv('data/featured_weather_data.csv')
print("Feature engineering complete! Data saved to 'data/featured_weather_data.csv'")
