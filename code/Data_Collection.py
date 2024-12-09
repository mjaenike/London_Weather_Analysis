# Importing standard libraries
import pandas as pd
import time

# Importing custom libraries
from Analysis_Functions import *

# Creating a DF of world cities
cities_df = pd.read_csv('country-capital-lat-long-population.csv')

# Initialize an empty list to store raininess index values
raininess_values = []

# Loop through each row in the DataFrame
for index, row in cities_df.iterrows():
    try:
        # Calculate the raininess index for the current city
        raininess_index = raininess({
            "City": row['Capital City'],
            "Country": row['Country'],
            "Historical Precipitation": get_historical_precipitation(row['Latitude'], row['Longitude']),
            "Forecast Precipitation": get_forecast_precipitation(row['Latitude'], row['Longitude'])
        })

        # Add a delay between each request to avoid hitting rate limits
        time.sleep(5)
        
    except KeyError as e:
        # Log an error message and skip to the next iteration
        print(f"KeyError for {row['Capital City']}, {row['Country']}: {e}")
        raininess_index = None  # Optional: assign None or a default value if data is missing
    
    # Append the calculated raininess index (or None) to the list
    raininess_values.append(raininess_index)

cities_df['Raininess'] = raininess_values

# Sort the cities by raininess index
cities_df = cities_df.sort_values(by='Raininess', ascending=False)

# Reset the index and remove the old one
cities_df = cities_df.reset_index(drop=True)

# Set the index to start at 1 instead of 0
cities_df.index = cities_df.index + 1

# Select only the relevant columns to display
sample_cities_df = cities_df[['Capital City', 'Country', 'Latitude', 'Longitude', 'Raininess']]

# Display the top 10 rainiest cities
print("Top 10 Rainiest Capital Cities:")
print(sample_cities_df.head(10))

# Save the DataFrame to a CSV file
cities_df.to_csv('rainiest_cities.csv', index=False)

