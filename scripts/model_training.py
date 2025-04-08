from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Define features and target
X = data[['air_temp', 'windspeed', 'winddir', 'pressure', 'humidity', 'rainfall', 'fog', 'temp_rolling_mean', 'temp_diff']]
y = data['air_temp'].shift(-1).dropna()
X = X[:-1]  # Align features with target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Save the model
import joblib
joblib.dump(model, 'weather_model.pkl')
