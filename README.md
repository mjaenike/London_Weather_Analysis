# <center>Is London Really as Rainy as the Movies Make It Out To Be? An Exploratory Data Analysis</center> 
This repository attempts to determine whether London's reputation as an ever-gray, rainy city accurately reflects its weather patterns.

***

## How to run the code
The code and its testing are most well documented in the [Jupyter Notebook](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/Weather_Data_Processing.ipynb). There is also a [.py file](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/Analysis_Functions.py) for the functions imported into the Jupyter Notebook. The testing of these functions is also included in the .py file. Lastly, there is a [.py file for Data Collection](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/Data_Collection.py).

To run the code, libraries must be installed in the terminal as follows:

```
>>> pip install <library>
```

These libraries include pandas, lets_plot, and geopandas.

Ensure both CSVs ([world_cities.csv](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/world_cities.csv) and [country-capital-lat-long-population.csv](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/country-capital-lat-long-population.csv)) are downloaded, as well as the .py files ([Analysis_Functions.py](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/Analysis_Functions.py) and [Data_Collection.py](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/Data_Collection.py)).

In the terminal command line, type:

```
>>> python Data_Collection.py
```

**NB:** Because of OpenMeteo's API request rate limiting policies, this file takes a significant amount of time (20.8 minutes) to produce the resulting CSV, [rainiest_cities.csv](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/rainiest_cities.csv). As such, the rainiest_cities.csv file can be downloaded from this repository directly.

Once the rainiest_cities CSV is downloaded, the visualizations included in the [Jupyter Notebook](https://github.com/lse-ds105/ds105a-2024-w06-summative-mjae-1616/blob/main/Weather_Data_Processing.ipynb) can be run using the "Run All" button in the notebook.

## References and Sources
The Wikipedia page entitled ["List of countries by average annual precipitation"](https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation) was used in the creation of the raininess index to verify that results reflected one of the metrics used in the calculation of the index (mm of rainfall)

Additionally, much of the knowledge of Python and some packages (namely, datetime, math, and time) was derived from previous coursework.

GitHub Copilot was used to produce the visualizations to debug some of the plotting and generate some formatting for the histogram visualization. Additionally, ChatGPT was used to help narrow down and prepare the data for the line graph.
