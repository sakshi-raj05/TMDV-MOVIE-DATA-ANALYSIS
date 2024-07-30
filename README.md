# Movie Success Prediction Project

This project aims to analyze a movie dataset to identify the kinds of movies that perform well in cinemas, the genres they belong to, and other factors influencing their success. This analysis will help the production company predict if a movie will be a commercial success, if it will be highly rated, and so on.

## Table of Contents

- [Introduction](#introduction)
- [Dataset Description](#dataset-description)
- [Implementation Tasks](#implementation-tasks)
- [Usage](#usage)
## Introduction

Movies with production budgets exceeding $100 million can still fail at the box office for various reasons. Movie lovers have different interests, and not all high-budget movies resonate with audiences. This project aims to uncover the underlying factors that affect movie success, including audience preferences, marketing strategies, critical reception, and cultural relevance.

## Dataset Description

The dataset used in this project contains the following columns:

- **budget**: The budget of the movie.
- **genres**: A list of genres associated with the movie.
- **homepage**: The URL of the movie's official homepage.
- **id**: The unique identifier of the movie.
- **keywords**: A list of keywords associated with the movie.
- **original_language**: The original language of the movie.
- **original_title**: The original title of the movie.
- **overview**: A brief overview or synopsis of the movie.
- **popularity**: The popularity score of the movie.
- **production_companies**: A list of production companies involved in the movie.
- **production_countries**: A list of production countries associated with the movie.
- **release_date**: The release date of the movie.
- **revenue**: The revenue generated by the movie.
- **runtime**: The duration of the movie in minutes.
- **spoken_languages**: A list of spoken languages in the movie.
- **status**: The status of the movie (e.g., Released, In Production).
- **tagline**: The tagline or slogan of the movie.
- **title**: The title of the movie.
- **vote_average**: The average rating of the movie.
- **vote_count**: The number of votes received by the movie.

## Implementation Tasks

The project consists of the following tasks:

1. **Load the Dataset**:
   - Load the movie dataset in the Python notebook.
   - Display the number of rows and columns in the dataset.
   - Display the titles and genres of the first 50 movies.

2. **Handle Missing Values**:
   - Identify the columns that have null values.
   - Perform the appropriate null value treatment based on the type of data in the columns of interest.

3. **Filter by Budget**:
   - Display the movie categories with a budget greater than $220,000.

4. **Filter by Revenue**:
   - Display the movie categories where the revenue is greater than $961,000,000.

5. **Remove Zero Values**:
   - Remove the rows where the budget and revenue columns have the value 0.

6. **Top Movies by Revenue and Budget**:
   - List the top 10 movies with the highest revenues.
   - List the top 10 movies with the least budget.

7. **Popularity and Budget Correlation**:
   - Analyze the relationship between the popularity of movies and their budgets.
   - Determine if they are correlated or uncorrelated.
   - Write the interpretation of your analysis.

8. **Production Companies Frequency**:
   - Identify and display the names of all production companies along with the number of times they appear in the dataset.

9. **Top Production Companies**:
   - Display the names of the top 25 production companies based on the number of movies they have produced, in descending order.

10. **Revenue-Based Sorting and Analysis**:
    - Sort the data in descending order based on revenue.
    - Filter the top 500 movies.
    - Calculate measures of central tendency (mean, median, mode) for budget, revenue, and runtime.
    - Perform outlier analysis for the budget, revenue, and runtime columns using box plots.

11. **Above Average Runtime Movies**:
    - Identify and display the names of the movies along with their run times for those movies that have above-average runtime, using the data from the previous tasks.

## Usage

To use this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movies-success-prediction.git

2. Navigate to the project directory:
  ```bash
  cd movies-success-prediction

3. Install the required dependencies:
  ```bash
  pip install -r requirements.txt

4. Run the analysis scripts:
  ```bash
  jupyter notebook





