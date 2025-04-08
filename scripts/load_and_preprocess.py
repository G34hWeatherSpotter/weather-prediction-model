import pandas as pd

# Load data
data = pd.read_csv('data/weather_data.csv', sep='\t')  # Assuming tab-separated values (TSV)

# Debug: Print column names to ensure they match the expected format
print("Column Names in Dataset:", data.columns)

# Strip any extra spaces from column names
data.columns = data.columns.str.strip()

# Ensure the column names match the expected format
expected_columns = ['Year', 'Month', 'Day', 'Hour', 'air_temp', 'windspeed', 'winddir', 'pressure', 'humidity', 'rainfall', 'fog', 'AOD']
if not all(col in data.columns for col in expected_columns):
    raise ValueError(f"Dataset is missing one or more of the expected columns: {expected_columns}")

# Create a datetime column and set as index
data['datetime'] = pd.to_datetime(data[['Year', 'Month', 'Day', 'Hour']])
data = data.set_index('datetime')

# Drop unnecessary columns
data = data.drop(columns=['Year', 'Month', 'Day', 'Hour', 'AOD'])

# Save cleaned data for later use
data.to_csv('data/cleaned_weather_data.csv')
print("Preprocessing Complete! Cleaned data saved to 'data/cleaned_weather_data.csv'")
