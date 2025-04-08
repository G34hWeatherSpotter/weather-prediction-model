import pandas as pd

# Load data
data = pd.read_csv('data/weather_data.csv')

# Debug: Print column names to check
print("Column Names:", data.columns)

# Data preprocessing
data['datetime'] = pd.to_datetime(data[['Year', 'Month', 'Day', 'Hour']])
data = data.set_index('datetime')
data = data.drop(columns=['Year', 'Month', 'Day', 'Hour', 'AOD'])

# Save cleaned data for later scripts
data.to_csv('data/cleaned_weather_data.csv')
print("Preprocessing Complete!")
