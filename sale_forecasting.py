import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Load historical sales data
data = pd.read_csv('sales_data.csv')

# Data preprocessing and transformation
data['Month'] = data['Month'].map(month_to_num)
data['date'] = pd.to_datetime(data[['Year', 'Month', 'Day']])
data.set_index('date', inplace=True)
sales_data = data[['Revenue']]

# Split data into training and testing sets
train_size = int(0.8 * len(sales_data))
train, test = sales_data[:train_size], sales_data[train_size:]

# Plot ACF and PACF to determine model orders
# (Code for plotting ACF and PACF)

# Fit ARIMA model
order = (2, 1, 2)  # Replace with appropriate values for your data
model = ARIMA(train, order=order)
model_fit = model.fit()

# Forecast
forecast_steps = len(test)
forecast = model_fit.forecast(steps=forecast_steps)

# Plot the forecasted results
plt.plot(test.index, test.values, label='Actual')
plt.plot(test.index, forecast, label='Forecast', color='red')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Forecast using ARIMA')
plt.legend()
plt.show()

# Calculate forecast accuracy metrics (e.g., MAE, RMSE)
mae = np.mean(np.abs(test.values - forecast))
rmse = np.sqrt(np.mean((test.values - forecast)**2))
print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")
