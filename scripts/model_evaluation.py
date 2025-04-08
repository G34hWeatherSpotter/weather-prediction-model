import matplotlib.pyplot as plt

# Plot actual vs predicted temperatures
plt.figure(figsize=(10, 5))
plt.plot(y_test.index, y_test, label='Actual')
plt.plot(y_test.index, y_pred, label='Predicted', alpha=0.7)
plt.legend()
plt.title('Actual vs Predicted Temperatures')
plt.show()
