# <center>Is London Really as Rainy as the Movies Make It Out To Be? An Exploratory Data Analysis</center> 
This repository attempts to answer the question of whether London's reputation as an ever-gray, rainy city accurately reflects its weather patterns.

## Part 1: The Approach
To answer this question, it must first be determined what London should be compared *to*. Of course, there are many possible approaches, each yielding varying answers. The method I thought was most interesting was to compare London to cities spread across the globe. A convenient way to do this would be to compare London to the other capital cities of the world; this would ensure a widely dispersed set of data while including many of the most populous cities (e.g., Paris, Tokyo, etc.). I would then, based on the data (see Part 2), define a "Raininess Index" (see Part 3) to easily compare the raininess of London to other world capitals and create meaningful visualizations of these analyses.

## Part 2: The Data
The data used for testing and the final analyses are contained in the [world_cities.csv](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/world_cities.csv) and the [country-capital-lat-long-population.csv](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/country-capital-lat-long-population.csv). The [OpenMeteo API](https://open-meteo.com/) provided the weather data, given the latitude and longitude of cities.

The DS105A LSE course provided the World Cities CSV; it contains data on city names, their country abbreviations, and their coordinates. This proved useful for testing many functions.

The country-capital-lat-long-population CSV was found on [GitHub Gist](https://gist.github.com/ofou/df09a6834a8421b4f376c875194915c9). This contains much of the same data as the World Cities CSV, but only includes the capital cities of each country. This made it easier to iterate through when requesting data from the OpenMeteo API.

The OpenMeteo API is a free API providing the historical and forecast weather data used in creating the raininess index; however, the API does have a rate limit. This is addressed in Part 3. Both historical and forecast weather data were collected for each capital city. Historical data included the past two years of daily rain sum (mm of rain per day) and hours of precipitation. The forecast data included the projected next 7 days of rain sum (mm of rain per day).

## Part 3: The Data Analysis

#### The Raininess Index
A raininess index was then defined; the past year of weather data was weighted equally (i.e., yesterday's weather influences the index just as much as the weather 365 days ago; this strategy was implemented so as to prevent a skew between the Northern and Southern hemisphere), while the year prior was weighted (equally) less (i.e., 366 days ago is weighted the same amount as 730 days ago, both of which are weighted less than 364 days ago). Forecast data can be very temperamental and non-reflective of true weather patterns, and as such is weighted the least.

Finally, the index was scaled down using a logarithmic scale.

#### Capital City Raininess
Using the capital city coordinate data, the raininess index was applied to each capital city and stored in a pandas DataFrame.

#### Visualizations
***[include when done]***

## Part 4: The Results

## Part 5: Conclusion

## Part 6: Limitations and Future Work

***

## How to run the code
The code and its testing are most well documented in the Jupyter Notebook ***[link here]***. There is also a .py file ***[link here]*** for the functions that were imported into the Jupyter Notebook ***[link here]***. The testing of these functions is also included in the .py file ***[link here]***.

## References and Sources
The Wikipedia page entitled ["List of countries by average annual precipitation"](https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation) was used in the creation of the raininess index to very that results reflected one of the metrics used in the calculation of the index (mm of rainfall)

Additionally, much of the knowledge of Python and some packages (namely, datetime, math, and time) was derived from previous coursework.
