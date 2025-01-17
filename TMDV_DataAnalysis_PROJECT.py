#!/usr/bin/env python
# coding: utf-8

# # TMDV MOVIE DATA ANALYSIS

# In[38]:


import numpy as np
import pandas as pd
import seaborn as sns
import json
import warnings
warnings.filterwarnings("ignore")
import statistics as st
import matplotlib.pyplot as plt


# # TASK 1
# Load the movie dataset in the python notebook. Display the numbers of rows and columns in the dataset. Display the titles and genres of the first 50 movies.

# In[39]:


# loading the dataset
df = pd.read_csv('DS1_C8_V3_ND_Sprint2_Data Analysis Using Python_Dataset.csv')
df.head()


# In[40]:


# displaying the number of rows and columns
df.shape


# In[41]:


# Extract titles and genres for the first 50 movies
titles_and_genres = df[['title', 'genres']].head(50)

# Display the titles and genres
titles_and_genres


# In[42]:


# Heat Map : To visually represent the correlation between variables in a dataset.


# In[43]:


columns_of_interest = ['budget', 'revenue', 'popularity', 'runtime', 'vote_average', 'vote_count']
subset_df = df[columns_of_interest]
subset_df


# In[44]:


correlation_matrix = subset_df.corr()
correlation_matrix


# In[45]:


plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# # Interpretation : 
# * 'budget' and 'revenue' have a strong positive correlation of 0.73. This suggests that there is a significant relationship between the budget allocated to a movie and the revenue it generates. Movies with higher budgets tend to generate higher revenues.
# 
# 
# * 'revenue' and 'popularity' also have a strong positive correlation of 0.64. This indicates that movies with higher revenues tend to be more popular among audiences.
# 
# 
# * 'popularity' and 'vote_count' exhibit a strong positive correlation of 0.78. This implies that movies with higher popularity, as measured by factors such as online views, social media engagement, or user ratings, tend to receive a higher number of votes.
# 
# 
# * The correlation between 'budget' and 'popularity' is 0.51, indicating a moderate positive relationship. This suggests that movies with higher budgets are more likely to gain popularity among audiences.
# 
# 
# * There is a relatively weak positive correlation between 'runtime' and 'vote_average' (0.37) and between 'popularity' and 'vote_average' (0.27). This suggests that there is a slight tendency for movies with longer runtimes or higher popularity to have slightly higher average votes, but the relationship is not very strong.
# 
# 
# * The correlation between 'vote_average' and 'vote_count' is 0.31, indicating a moderate positive relationship. This suggests that movies with higher average votes tend to receive a higher number of votes.

# In[46]:


# Scatter plot of budget vs. revenue
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='budget', y='revenue')
sns.regplot(data=df, x='budget', y='revenue', scatter=False, color='red')
plt.title('Budget vs. Revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.show()


# # Interpretation : 
# * Positive Relationship: The trend line in the graph has a positive slope, indicating a positive relationship between the movie's budget and its revenue. This means that, in general, movies with higher budgets tend to generate higher revenues.
# 
#     
# * Scatter of Data Points: The data points on the scatter plot are spread out, suggesting some variability in the relationship between budget and revenue. While there is a positive trend, it's important to note that the actual revenue generated by a movie can vary even within a similar budget range.
# 
#     
# * Outliers: The scatter plot may contain outliers, which are data points that deviate significantly from the general trend. These outliers could represent movies that achieved unexpectedly high or low revenues compared to their budgets.  

# In[47]:


# Scatter plot of revenue vs. popularity
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='popularity', y='revenue')
sns.regplot(data=df, x='popularity', y='revenue', scatter=False, color='red')
plt.title('Revenue vs. Popularity')
plt.xlabel('Popularity')
plt.ylabel('Revenue')
plt.show()


# # Interpretation : 
# 
# * Positive Relationship: The trend line has a positive slope, it indicates a positive relationship between revenue and popularity. This means that movies with higher popularity tend to generate higher revenues.
# 
#     
# * Scatter of Data Points: The data points on the scatter plot represent individual movies, and their distribution around the trend line shows the variability in the relationship. A tighter cluster of points around the trend line suggests a stronger relationship, while a more scattered distribution indicates a weaker relationship.
# 
#     
# * Outliers: The scatter plot may contain outliers, which are data points that deviate significantly from the general trend line. These outliers could represent movies that achieved unusually high or low revenues compared to their popularity levels.

# In[48]:


# Scatter plot of popularity vs. vote_count
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='popularity', y='vote_count')
sns.regplot(data=df, x='popularity', y='vote_count', scatter=False, color='red')
plt.title('Popularity vs. Vote Count')
plt.xlabel('Popularity')
plt.ylabel('Vote Count')
plt.show()


# # Interpretation :
# 
# 
# * Positive Relationship: The trend line has a positive slope, it indicates a positive relationship between popularity and vote count. This means that movies with higher popularity tend to receive a higher number of votes.
# 
#     
# * Scatter of Data Points: The data points on the scatter plot represent individual movies, and their distribution around the trend line shows the variability in the relationship. A tighter cluster of points around the trend line suggests a stronger relationship, while a more scattered distribution indicates a weaker relationship.
# 
#     
# * Outliers: The scatter plot may contain outliers, which are data points that deviate significantly from the general trend line. These outliers could represent movies that achieved unexpectedly high or low vote counts compared to their popularity levels.

# In[49]:


# Scatter plot of budget vs. popularity
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='budget', y='popularity')
sns.regplot(data=df, x='budget', y='popularity', scatter=False, color='red')
plt.title('Budget vs. Popularity')
plt.xlabel('Budget')
plt.ylabel('Popularity')
plt.show()


# # Interpretation :
# 
# 
# * Positive Relationship: The scatter plot shows a general positive trend, indicating that higher budgets tend to be associated with higher popularity for movies. This suggests that movies with larger budgets have a higher likelihood of attracting attention and interest from audiences.
# 
# 
# * Outliers: Some data points deviate from the overall trend, representing movies with unexpectedly high or low popularity given their budgets. These outliers may indicate unique cases where factors other than budget contribute significantly to a movie's popularity.
# 
# 
# * Trend Line: The red trend line represents the estimated relationship between budget and popularity. It provides a visual representation of the overall trend and helps identify the direction of the relationship. The upward slope of the trend line confirms the positive correlation between budget and popularity.
# 
# 
# * Variability: While there is a positive relationship, there is also variability in popularity within similar budget ranges. This suggests that factors beyond budget, such as marketing strategies, cast, genre, or storyline, may influence a movie's popularity.

# # Overall Conclusion : 
# 
# 
# * Budget vs. Revenue:
# 
# There is a positive relationship between a movie's budget and its revenue.
# Movies with higher budgets tend to generate higher revenues.
# However, there is some variability in revenue even within similar budget ranges.
# Outliers may exist, representing movies with unexpectedly high or low revenues compared to their budgets.
# 
# 
# * Revenue vs. Popularity:
# 
# There is a positive relationship between a movie's revenue and its popularity.
# Movies with higher popularity tend to generate higher revenues.
# The relationship between revenue and popularity appears to be stronger compared to other factors.
# Outliers may exist, representing movies with unusually high or low revenues given their popularity.
# 
# 
# * Popularity vs. Vote Count:
#     
# There is a positive relationship between a movie's popularity and its vote count.
# Movies with higher popularity tend to receive a higher number of votes.
# The relationship between popularity and vote count indicates that popular movies tend to engage more audiences who vote for them.
# Outliers may exist, representing movies with unexpectedly high or low vote counts given their popularity.
# 
# * Budget vs. Popularity:
# 
# The relationship between a movie's budget and its popularity appears to be more varied.
# While there is no clear trend or strong relationship, some movies with higher budgets may achieve higher popularity.
# However, the scatter plot shows more variability and less clustering around the trend line, suggesting a weaker relationship.
# Outliers may exist, representing movies with unexpectedly high or low popularity given their budget.

# # Task 2
# Identify the columns that have null values and perform the null value treatment. (choose the imputation method based on the type of data in the columns of interest).

# In[50]:


# identifying the columns with null values
df.isnull().sum()


# In[51]:


df['homepage'].fillna(df['homepage'].mode()[0], inplace= True)


# In[52]:


df['tagline'].fillna(df['tagline'].mode()[0], inplace= True)


# In[53]:


df['overview'].fillna(df['overview'].mode()[0], inplace= True)


# In[54]:


df['release_date'].fillna(df['release_date'].mode()[0], inplace= True)


# In[55]:


df['runtime'].fillna(df['runtime'].mean(), inplace= True)


# In[56]:


# checking for null values after imputation
df.isnull().sum()


# # Task 3
# Display the movie categories that have a budget greater than 220,000.

# In[57]:


# Filter movies with budget greater than 220,000
filtered_movies = df[df['budget'] > 220000]
filtered_movies[['title']]


# # Task 4 and 5
# In the dataset, there are some movies for which the budjet and revenue columns have the value 0, which mean unknown values. Remove the rows with value 0 from both the budget and revenue columns

# In[58]:


# Remove rows with value 0 in both budget and revenue columns
df = df[(df['budget'] != 0) & (df['revenue'] != 0)]

# Reset the index
df.reset_index(drop=True, inplace=True)
df


# # Task 6
# List the top 10 movies with the highest revenues and the top 10 movies with the least budget.

# In[59]:


top_10_revenue = df.sort_values('revenue', ascending=False).head(10)
print("Top 10 Movies with Highest Revenues:")
top_10_revenue[['title', 'revenue']]


# In[82]:


# Plotting the bar graph
plt.figure(figsize=(10, 6))
sorted_data = top_10_revenue.sort_values('revenue', ascending=True)  # Sort the data in descending order
plt.barh(sorted_data['title'], sorted_data['revenue'])
plt.xlabel('Revenue')
plt.ylabel('Movie Title')
plt.title('Top 10 Movies with Highest Revenues')
plt.tight_layout()
plt.show()


# In[61]:


top_10_budget = df.sort_values('budget', ascending=True).head(10)
print("\nTop 10 Movies with Least Budget:")
top_10_budget[['title', 'budget']]


# In[83]:


# Plotting the bar graph
plt.figure(figsize=(10, 6))
plt.barh(top_10_budget['title'], top_10_budget['budget'])
plt.xlabel('Movie Title')
plt.ylabel('Budget')
plt.title('Top 10 Movies with Least Budgets')
plt.tight_layout()

# Displaying the bar graph
plt.show()


# In[86]:


# Plotting the bar graph
plt.figure(figsize=(10, 6))
sorted_data = top_10_budget.sort_values('budget', ascending=False)  # Sort the data in ascending order
plt.barh(sorted_data['title'], sorted_data['budget'])
plt.xlabel('Budget')
plt.ylabel('Movie Title')
plt.title('Top 10 Movies with Least Budgets')
plt.tight_layout()

# Displaying the bar graph
plt.show()


# # Task 7
# How are the popularities of movies related with the movie budgets? Are they correlated or totally uncorrelated with each other? Write the interpretation of your analysis.

# In[63]:


# extracting the columns
popularity = df['popularity']
budget = df['budget']


# In[64]:


# calculating correlation coefficient
correlation = popularity.corr(budget)
print("Correlation coefficient:", correlation)


# In[65]:


# Visualize the relationship using a scatter plot
plt.scatter(budget, popularity)
plt.xlabel('budget')
plt.ylabel('popularity')
plt.title('Relationship between Movie Popularity and Budget')
plt.show()


# In[66]:


# Calculate the trend line using numpy.polyfit
trend = np.polyfit(budget, popularity, 1)
trend_line = np.poly1d(trend)

# Visualize the relationship using a scatter plot with the trend line
plt.scatter(budget, popularity)
plt.plot(budget, trend_line(budget), color='red', linestyle='--', label='Trend Line')
plt.xlabel('budget')
plt.ylabel('popularity')
plt.title('Relationship between Movie Popularity and Budget')
plt.legend()
plt.show()


# # Interpretation : 
# 
# 1. Correlation Coefficient:
# 
# * The correlation coefficient of 0.43 suggests a positive correlation between movie popularity and budget, but the correlation is moderate.
# * This positive correlation indicates that, on average, as the budget increases, there tends to be a tendency for movies to have slightly higher popularity scores.
# * However, it's important to note that the correlation coefficient of 0.43 suggests that other factors, apart from the budget, also contribute to movie popularity, as there is still significant variation in popularity scores even within similar budget levels.
# 
# 2. Scatter Plot:
# 
# * The data points are scattered across the plot, indicating that there is some variation in the popularity of movies across different budget levels.
# * There is a general trend of movies with higher budgets having slightly higher popularity scores, but the relationship is not extremely strong or consistent.
# 
# 3. Trend Line:
# 
# * In this case, the trend line is positive, indicating a positive correlation between movie popularity and budget. As the budget increases, there is a tendency for movies to have slightly higher popularity scores on average.
# * However, it's important to note that the trend line represents a general trend in the data, and there will still be variation and individual differences among movies with similar budgets.
# 
# 
# 
# 
# Overall, the scatter plot with the trend line and the correlation coefficient suggests a moderate positive relationship between movie popularity and budget. While higher budgets may contribute to increased popularity on average, it's important to consider that other factors can influence movie popularity as well, and there will be variations within different budget levels.

# # Task 8
# Identify and display the names of all production companies along with the number of times they appear in the dataset.

# In[67]:


# filter the data
df = df[(df['production_companies'] != '[]')]

# Reset the index of the DataFrame
df.reset_index(drop=True, inplace = True)


# In[68]:


df['production_companies'] = df['production_companies'].apply(json.loads)


# In[69]:


df['Production_Company'] = df['production_companies'].apply(lambda x : [i['name'] for i in x])


# In[70]:


# display the names of all production companies along with the number of times they appear
df_companies = df['Production_Company'].explode().value_counts()
df_companies


# # Task 9
# Display the names of the top 25 production companies based on the number of movies they have produced in descending order of the number of movies produced.

# In[71]:


df_companies_top25 = df_companies.head(25)
df_companies_top25


# In[72]:


# Create the figure and axis objects
fig, ax = plt.subplots()

# Plot the horizontal bar graph
ax.barh(df_companies_top25.index, df_companies_top25.values)

# Set the axis labels and title
ax.set_xlabel('Number of Movies')
ax.set_ylabel('Production Company')
ax.set_title('Top 25 Production Companies by Number of Movies')

# Invert the y-axis to display the highest count at the top
ax.invert_yaxis()

# Adjust the layout to prevent overlapping labels
plt.tight_layout()

# Show the plot
plt.show()


# # Task 10
# Sort the data in descending order based on revenue and filter the top 500 movies. Find the measures of central tendency for the following columns using the filtered data:
# 1. budget
# 2. revenue
# 3. runtime
# 
# Perform the outlier analysis for the above three columns using box plots.

# In[73]:


# Sort the data in descending order based on revenue
sorted_df = df.sort_values(by='revenue', ascending=False)

# Filter the top 500 movies
top_500_movies = sorted_df.head(500)
top_500_movies


# In[74]:


# Calculate the measures of central tendency for budget column
budget_mean = top_500_movies['budget'].mean()
budget_median = top_500_movies['budget'].median()
budget_mode = top_500_movies['budget'].mode().values[0]

print("Budget:")
print("Mean:", budget_mean)
print("Median:", budget_median)
print("Mode:", budget_mode)


# In[75]:


# Calculate the measures of central tendency for revenue column
revenue_mean = top_500_movies['revenue'].mean()
revenue_median = top_500_movies['revenue'].median()
revenue_mode = top_500_movies['revenue'].mode().values[0]

print("Revenue:")
print("Mean:", revenue_mean)
print("Median:", revenue_median)
print("Mode:", revenue_mode)


# In[76]:


# Calculate the measures of central tendency for runtime column
runtime_mean = top_500_movies['runtime'].mean()
runtime_median = top_500_movies['runtime'].median()
runtime_mode = top_500_movies['runtime'].mode().values[0]

print("Runtime:")
print("Mean:", runtime_mean)
print("Median:", runtime_median)
print("Mode:", runtime_mode)


# In[102]:


# Perform outlier analysis using box plots
plt.figure(figsize=(15, 10))
plt.boxplot([top_500_movies['budget'], top_500_movies['revenue'], top_500_movies['runtime']], labels=['Budget', 'Revenue', 'Runtime'])
plt.title('Outlier Analysis')
plt.xlabel('Columns')
plt.ylabel('Values')
plt.show()


# # Interpretation :
# 
# 1. Budget
# 
# * The box plot for the 'Budget' column shows that the median value is relatively high, indicating that most movies in the top 500 have relatively high budgets.
# * There are a few outliers that have exceptionally high budgets.
# * The presence of outliers suggests that there are a few movies within the top 500 with extremely high budgets, potentially indicating big-budget productions or blockbuster films.
# 
# 2. Revenue:
# 
# * The box plot for the 'Revenue' column shows that the median value is relatively high, indicating that the median revenue for the top 500 movies is substantial.
# * The interquartile range (IQR) is quite wide, indicating a significant variation in revenue among the top movies.
# * There are a few outliers with extremely high revenue values.
# * The presence of outliers suggests that there are some movies within the top 500 that have generated exceptional revenue, potentially indicating highly successful or blockbuster films.
# 
# 3. Runtime:
# 
# * The interquartile range (IQR) is relatively narrow, suggesting that the majority of movies in the top 500 have runtimes within a similar range.
# * The presence of outliers suggests that there are a few movies within the top 500 that deviate from the typical runtime duration, either being shorter or longer than average.

# # Task 11
# Identify and display the names of the movies along with their run times for those movies that have above average runtime, using the data from the previous task.

# In[78]:


# Filter the movies with above-average runtime
above_average_runtime_movies = top_500_movies[top_500_movies['runtime'] > runtime_mean]

# Display the names of movies along with their runtimes
movie_names_runtimes = above_average_runtime_movies[['title', 'runtime']]
print(movie_names_runtimes)


# In[121]:


# some extra graphs for better analysis and presentation work


# In[116]:


# Sort the dataset by vote count and select the top 10 movies
top_10_vote_count = df.sort_values('vote_count', ascending=False).head(10)

# Create a bar graph for the top 10 movies by vote count
plt.figure(figsize=(10, 6))
plt.barh(top_10_vote_count['title'], top_10_vote_count['vote_count'], color='orange')
plt.title('Top 10 Movies by Vote Count')
plt.xlabel('Movie')
plt.ylabel('Vote Count')
plt.show()


# In[119]:


# Sort the dataset by popularity and select the top 10 movies
top_10_popularity = df.sort_values('popularity', ascending=False).head(10)

# Create a bar graph for the top 10 movies by popularity
plt.figure(figsize=(10, 6))
plt.barh(top_10_popularity['title'], top_10_popularity['popularity'], color='orange')
plt.title('Top 10 Movies by Popularity')
plt.xlabel('Popularity')
plt.ylabel('Movie')
plt.show()

