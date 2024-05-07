# sqlalchemy-challenge

## Introduction
This project involves conducting a climate analysis for Honolulu, Hawaii, to aid in trip planning. The analysis is divided into two primary sections. The first part involves analyzing and exploring climate data, where SQLAlchemy is employed to connect to a SQLite database. Precipitation and station analyses are conducted, along with data exploration using Pandas and Matplotlib. The second part involves designing a Flask API based on the queries developed in the first part. This includes creating routes to retrieve specific climate data through API endpoints

## Dependencies

This project requires the following dependencies to be installed:

- [Flask]: Used for creating the web application and API endpoints.
- [SQLAlchemy]: Utilized for database management and querying.
- [datetime]: Used for working with dates and times.


### Folder Structure 

The sqlalchemy-challenge consists of the following folders and files:

**Resources**: Contains the Hawaii.sqlite database, hawaii_measurements.csv and hawaii_stations.csv files.

**climate_starter.ipynb**: A Jupyter Notebook file containing analysis and exploration of Climate Data.

**app.py**: Contains routes to retrieve specific climate data through API endpoints.

**README.md**: Overview of the project.

**sqlalchemy-challenge_screenshots.docx**: Provides screenshots of the analysis results obtained after executing `climate_starter.ipynb` and 'app.py'.


## Instructions

**To run the climate_starter.ipynb, follow these steps:**

1.Clone the GitHub repository to your local machine using the following command:

   git clone https://github.com/SriPenumatcha/sqlalchemy-challenge.git

2.Open the climate_starter.ipynb file using Jupyter Notebook.

3.Run each cell in the notebook to execute the code and view the results.

4.Review the analysis findings.


**To run the app.py, follow these steps:**

1.Navigate to the project directory:

  cd sqlalchemy-challenge


2.Run the Python script using the following command:

  python app.py