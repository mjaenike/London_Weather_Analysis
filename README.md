# <center>Is London Really as Rainy as the Movies Make It Out To Be? An Exploratory Data Analysis</center> 
This project investigates London's reputation as a perpetually rainy city and explores whether its weather patterns align with this perception.

***

## Table of Contents
- [Project Overview](#project-overview)
- [How to Run the Code](#how-to-run-the-code)
- [Data Collection](#data-collection)
- [Libraries and Dependencies](#libraries-and-dependencies)
- [References and Sources](#references-and-sources)

---

## Project Overview

London has long been portrayed as a city with persistent rain. In this project, I explore the accuracy of this portrayal by analyzing historical weather data. By using the OpenMeteo API, I assess the average rainfall for cities worldwide, focusing on London, and compare it against other major cities to determine whether the "rainy" stereotype holds up.

The project uses a combination of data collection, cleaning, and visualization techniques to offer an insightful exploration of the weather patterns across cities globally.

***

## How to Run the Code

The code is organized across three Python files for easier management and testing:

- [Data Collection](code/Data_Collection.py)
- [Functions](code/Functions.py)
- [Data Processing](code/Data_Processing.ipynb) (Jupyter Notebook)

The Jupyter Notebook contains the primary analysis, including visualizations, based on the collected data. The `.py` files contain functions and testing for data processing and collection.

### Installation Instructions

Before running the project, you need to install the required libraries. Open the terminal and install the libraries as follows:

```bash
pip install pandas lets-plot geopandas
```

## Data Collection
To collect the necessary data, run the **Data_Collection.py** script. The script fetches data from OpenMeteo's API and saves it in a CSV file, which is then used for analysis. In the terminal, type the following command:

```
>>> python Data_Collection.py
```

**Note:** The OpenMeteo API has request rate limits, so this script will take approximately **20.8** minutes to complete. You can download the pre-collected data file directly from this repository: [rainiest_cities.csv.](data/rainiest_cities.csv)

Once the data is collected, run the Jupyter Notebook, [Data_Processing.ipynb](code/Data_Processing.ipynb), using the "Run All" button in the notebook to visualize and analyze the data.

## Libraries and Dependencies
The project uses the following Python libraries:

- **pandas:** For data manipulation and analysis.
- **lets-plot:** For creating interactive visualizations.
- **geopandas:** For geographic data handling and plotting.

These libraries can be installed via `pip` as shown in the **Installation Instructions.**

## References and Sources

- **OpenMeteo API:** Used for fetching weather data to analyze precipitation levels across cities.
- **Wikipedia:** The ["List of countries by average annual precipitation"](https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation) was used to verify that the results in the analysis reflect common precipitation metrics.

***

**Author:** Mia Jaenike<br>
**Contact:** miaajaenike@gmail.com<br>
**Last Updated:** 2024-12-11
