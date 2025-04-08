import pandas as pd

# Load data
data = pd.read_csv('data/weather_data.csv')

# Display the first few rows of the dataframe
print(data.head())

# Data preprocessing
# Drop rows with missing values
data = data.dropna()

# Convert date columns to datetime if not already
data['datetime'] = pd.to_datetime(data[['Year', 'Month', 'Day', 'Hour']])
data = data.set_index('datetime')

# Drop unnecessary columns
data = data.drop(columns=['Year', 'Month', 'Day', 'Hour', 'AOD'])

# Print the cleaned data
print(data.head())
