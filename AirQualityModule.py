import requests
import pandas as pd
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

current_datetime = datetime.datetime.now()
three_years_ago = current_datetime - datetime.timedelta(days=100)


# def check_stationarity(result):
#     result = adfuller(result, autolag='AIC')
#     print(f'ADF Statistic: {result[0]}')
#     print(f'p-value: {result[1]}')
#     print(f'Critical Values:')
#     for key, value in result[4].items():
#         print(f'{key}: {value}')


# def GetTheCuurentAirQualityDetailsForTheLocation(latitude, longitude):

#     url = 'http://api.openweathermap.org/data/2.5/air_pollution?lat={0}&lon={1}&appid=0edfea50656e01bcdf9934a88eb7243f'.format(
#         latitude, longitude)

#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#         return {"success": True, "response": data}

#     else:
#         return {"success": False, "response": "Internal Server Error"}


# GetTheCuurentAirQualityDetailsForTheLocation()


def check_stationarity(aqi_values):
    result = adfuller(aqi_values, autolag='AIC')
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    print(f'Critical Values:')
    for key, value in result[4].items():
        print(f'{key}: {value}')


def Get_PastAirQualityDetailsForTheLocation(latitude, longitude, start, end):
    url = 'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={0}&lon={1}&start={2}&end={3}&appid=0edfea50656e01bcdf9934a88eb7243f'.format(
        latitude, longitude, start, end)
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result = data["list"]
        aqi_values = [int(entry["main"]["aqi"]) for entry in result]

        resultnew = [{"Date": datetime.datetime.utcfromtimestamp(entry["dt"]).strftime('%Y-%m-%d'),
                      "AQI": int(entry["main"]["aqi"])}
                     for entry in result]
        new = pd.DataFrame(resultnew)
        # print(new)

        check_stationarity(aqi_values)

        data_diff = pd.Series(aqi_values).diff().dropna()
        # plt.figure(figsize=(12, 6))

        # plot_acf(data_diff, lags=20)
        # plt.title('Autocorrelation Function (ACF)')
        # plt.show()

        # plt.figure(figsize=(12, 6))
        # plot_pacf(data_diff, lags=20)
        # plt.title('Partial Autocorrelation Function (PACF)')
        # plt.show()

        # Fit the ARIMA model
        p = 1  # AR order
        d = 1  # Differencing order
        q = 1  # MA order

        model = sm.tsa.ARIMA(aqi_values, order=(p, d, q))
        results = model.fit()

        # Predict future AQI values
        forecast_steps = 10  # Adjust the number of steps as needed
        forecast = results.forecast(steps=forecast_steps)

        # Print the forecasted values
        print('Forecasted AQI Values:')
        print(forecast)
        # ff = forecast.to_frame()

        # print(ff)
        return resultnew
    else:
        print(response)
        print(f"Request failed with status code {response.status_code}")


# Get_PastAirQualityDetailsForTheLocation(
  #  12.966783432041685, 79.13811836586041, int(three_years_ago.timestamp()), int(current_datetime.timestamp()))

# Get_PastAirQualityDetailsForTheLocation(12.966783432041685, 79.13811836586041, int(
#     three_years_ago.timestamp()), int(current_datetime.timestamp()))
# Get_AirQualityDetailsForTheLocation(12.7948109, 79.0006410968549)
