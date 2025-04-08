# Feature Engineering
# Create rolling averages for temperature
data['temp_rolling_mean'] = data['air_temp'].rolling(window=3).mean()

# Create temperature differences
data['temp_diff'] = data['air_temp'].diff()

# Drop rows with NaN values created by rolling mean and diff
data = data.dropna()

# Print the data with new features
print(data.head())
