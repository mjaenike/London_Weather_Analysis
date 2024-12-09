######################################################################################################################################
# Functions for the collection of data and the raininess index
# Last Updated: Monday, November 4th, 2024
######################################################################################################################################
# Importing the required libraries
import requests
import datetime
import pandas as pd
import pprint
import math

######################################################################################################################################

def get_city_latlon(city, country):
    '''
    Get the latitude and longitude of a city in a country, derived from the world_cities CSV file.
    Params:
        city: str, the name of the city
        country: str, the name of the country
    Returns:
        a tuple of the latitude and longitude
    '''
    # Read the world_cities CSV file
    world_cities = pd.read_csv('world_cities.csv')

    # Filter the dataframe based on the city and country
    filtered_cities = world_cities[(world_cities['name'] == city) & (world_cities['country'] == country)]

    # Check if any matching cities are found
    if len(filtered_cities) > 0:
        # Get the longitude of the first matching city
        longitude = filtered_cities.iloc[0]['lng']
        # Get the latitude of the first matching city
        latitude = filtered_cities.iloc[0]['lat']
        # Return the latitude and longitude as a tuple
        return (latitude, longitude)
    else:
        # Return None if no matching city is found
        return None
    
######################################################################################################################################

def get_historical_precipitation(latitude: float, longitude: float) -> dict:
    '''
    Get the number of days rained and number of mm of rain in the past 2 years
    Params:
        latitude: float - latitude of the location
        longitude: float - longitude of the location
    Returns:
        a dictionary of the daily rain for the past 2 years in mm, number of hours of precipitation
    '''
    
    base_historical_url = "https://archive-api.open-meteo.com/v1/era5?"
    params_lat_long = f"latitude={latitude}&longitude={longitude}"

    current_date = datetime.date.today()
    five_years_ago = current_date - datetime.timedelta(days=365 * 5)
    start_date = five_years_ago.strftime("%Y-%m-%d")
    end_date = current_date.strftime("%Y-%m-%d")

    params_dates = f"&start_date={start_date}&end_date={end_date}"
    param_other = "&daily=rain_sum&daily=precipitation_hours"
    total_url = base_historical_url + params_lat_long + params_dates + param_other

    try:
        response = requests.get(total_url)
        historical_data = response.json()
        
        # Debugging: Print the entire response if 'daily' is missing
        if 'daily' not in historical_data:
            print(f"Full response for coordinates ({latitude}, {longitude}): {historical_data}")
            return {"Historical Rain Sum": [], "Historical Precipitation Hours": []}
        
        return {
            "Historical Rain Sum": historical_data['daily'].get('rain_sum', []),
            "Historical Precipitation Hours": historical_data['daily'].get('precipitation_hours', [])
        }

    except requests.exceptions.RequestException as e:
        print(f"Request failed for ({latitude}, {longitude}) with error: {e}")
        return {"Historical Rain Sum": [], "Historical Precipitation Hours": []}

######################################################################################################################################

def get_forecast_precipitation(latitude: float, longitude: float) -> dict:
    '''
    Get the hourly forecast precipitation for a given latitude and longitude for the next 7 days
    Params: 
        latitude: float - latitude of the location
        longitude: float - Longitude of the location
    Returns:
        dict - Forecast precipitation
    '''

    # Building the base URL
    base_forecast_url = "https://api.open-meteo.com/v1/forecast?"
    params_lat_long = "latitude=" + str(latitude) + "&longitude="  + str(longitude)
    params_others = "&daily=rain_sum"

    final_url = base_forecast_url + params_lat_long + params_others

    # Getting the forecast data
    response = requests.get(final_url)

    # Extracting the forecast precipitation
    forecast_data = response.json()
    forecast_precipitation = forecast_data['daily']['rain_sum']
    return forecast_precipitation

######################################################################################################################################

def raininess(data: dict) -> str:
    '''
    Calculate the raininess of a city based on the historical and forecast precipitation data
    Params:
        data: dict - a dictionary containing historical and forecast precipitation data
    Returns:
        int - the raininess of the city
    '''

    historical_rain_sum = data['Historical Precipitation']['Historical Rain Sum']
    historical_precipitation_hours = data['Historical Precipitation']['Historical Precipitation Hours']
    forecast_rain_sum = data['Forecast Precipitation']

    # Weights for each year of the historical data
    weights = [1, 0.5]

    # Split data into yearly chunks
    days_per_year = len(historical_rain_sum) // 2  # Assuming equal length data for each year
    weighted_rain_sum = 0
    weighted_precipitation_hours = 0

    # Calculate the weighted sum of the historical data
    for i, weight in enumerate(weights):
        start_idx = i * days_per_year
        end_idx = start_idx + days_per_year
        
        # Calculate the sum for this year's data
        year_rain_sum = sum(day for day in historical_rain_sum[start_idx:end_idx] if day is not None)
        year_precipitation_hours = sum(hour for hour in historical_precipitation_hours[start_idx:end_idx] if hour is not None)
        
        # Apply weights
        weighted_rain_sum += weight * year_rain_sum
        weighted_precipitation_hours += weight * year_precipitation_hours

    # Calculate the raininess index based on weighted values
    raininess_index = weighted_rain_sum + 0.3 * weighted_precipitation_hours

    # Add a small boost if there's significant rain in the forecast
    forecast_threshold = 5
    if any(rain >= forecast_threshold for rain in forecast_rain_sum):
        raininess_index += 10  # Small boost if there's rain in the forecast

    # Normalize the raininess index using a logarithmic scale
    log_base = 4
    multiplier = 10
    normalized_raininess_index = multiplier * math.log(raininess_index + 1, log_base)

    return normalized_raininess_index

######################################################################################################################################

def main() -> None:

    ######################################################################################################################################

    # Testing the get_city_latlon function

    # Test 1: Mumbai, India
    city = 'Mumbai'
    country = 'IN'
    print(f'The latitude and longitude of {city}, {country} is {get_city_latlon(city, country)}')

    # Test 2: New York City, United States
    city = 'New York City'
    country = 'US'
    print(f'The latitude and longitude of {city}, {country} is {get_city_latlon(city, country)}')

    # Test 3: Tokyo, Japan
    city = 'Tokyo'
    country = 'JP'
    print(f'The latitude and longitude of {city}, {country} is {get_city_latlon(city, country)}')

    # Test 4: Walnut Creek, United States
    city = 'Walnut Creek'
    country = 'US'
    print(f'The latitude and longitude of {city}, {country} is {get_city_latlon(city, country)}')

    ######################################################################################################################################

    # Testing historical precipitation using the get_historical_precipitation function and the get_city_latlon function

    # Test 1: San Francisco
    print("Test 1: San Francisco")
    city = 'San Francisco'
    country = 'US'
    latitude, longitude = get_city_latlon(city, country)
    pprint.pp(get_historical_precipitation(latitude, longitude))

    print("\n")
    print("-" * 20)
    print("\n")

    # Test 2: New York
    print("Test 2: New York City")
    city = 'New York City'
    country = 'US'
    latitude, longitude = get_city_latlon(city, country)
    pprint.pp(get_historical_precipitation(latitude, longitude))

    print("\n")
    print("-" * 20)
    print("\n")

    # Test 3: London
    print("Test 3: London")
    city = 'London'
    country = 'GB'
    latitude, longitude = get_city_latlon(city, country)
    pprint.pp(get_historical_precipitation(latitude, longitude))

    ######################################################################################################################################

    # Testing the get_forecast_precipitation function using the get_city_latlon function

    # Test 1: San Francisco
    city = 'San Francisco'
    country = 'US'
    latitude, longitude = get_city_latlon(city, country)
    print(get_forecast_precipitation(latitude, longitude))

    # Test 2: New York
    city = 'New York City'
    country = 'US'
    latitude, longitude = get_city_latlon(city, country)
    print(get_forecast_precipitation(latitude, longitude))

    # Test 3: London
    city = 'London'
    country = 'GB'
    latitude, longitude = get_city_latlon(city, country)
    print(get_forecast_precipitation(latitude, longitude))

    # Test 4: Mumbai
    city = 'Mumbai'
    country = 'IN'
    latitude, longitude = get_city_latlon(city, country)
    print(get_forecast_precipitation(latitude, longitude))

    # Test 5: Tokyo
    city = 'Tokyo'
    country = 'JP'
    latitude, longitude = get_city_latlon(city, country)
    print(get_forecast_precipitation(latitude, longitude))

    ######################################################################################################################################

    # Testing the raininess function

    # Test 1: London
    print("Raininess of London:")

    city = 'London'
    country = 'GB'
    latitude, longitude = get_city_latlon(city, country)

    London = {
        "City": 'London',
        "Country": 'GB',
        "Historical Precipitation": get_historical_precipitation(latitude, longitude),
        "Forecast Precipitation": get_forecast_precipitation(latitude, longitude)
    }
    
    print(raininess(London))

    print("-" * 20)

    # Test 2: San Francisco
    print("Raininess of San Francisco:")

    city = 'San Francisco'
    country = 'US'
    latitude, longitude = get_city_latlon(city, country)

    San_Francisco = {
        "City": 'San Francisco',
        "Country": 'US',
        "Historical Precipitation": get_historical_precipitation(latitude, longitude),
        "Forecast Precipitation": get_forecast_precipitation(latitude, longitude)
    }

    print(raininess(San_Francisco))

    print("-" * 20)

    # Test 3: New York

    print("Raininess of New York City:")
    city = 'New York City'
    country = 'US'
    latitude, longitude = get_city_latlon(city, country)

    New_York = {
        "City": 'New York City',
        "Country": 'US',
        "Historical Precipitation": get_historical_precipitation(latitude, longitude),
        "Forecast Precipitation": get_forecast_precipitation(latitude, longitude)
    }

    print(raininess(New_York))

    print("-" * 20)

    # Test 4: Mumbai
    print("Raininess of Mumbai:")
    city = 'Mumbai'
    country = 'IN'
    latitude, longitude = get_city_latlon(city, country)

    Mumbai = {
        "City": 'Mumbai',
        "Country": 'IN',
        "Historical Precipitation": get_historical_precipitation(latitude, longitude),
        "Forecast Precipitation": get_forecast_precipitation(latitude, longitude)
    }

    print(raininess(Mumbai))


if __name__ == '__main__':
    print('Testing Analysis_Functions.py')