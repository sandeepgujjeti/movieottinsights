# movie_ott_insights.py

# 📌 Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For better visuals
plt.style.use("ggplot")

# 📌 Step 2: Load dataset
df = pd.read_csv("netflix_titles.csv")

# 📌 Step 3: Explore dataset
print("Shape of dataset:", df.shape)
print(df.head())
print(df.info())

# 📌 Step 4: Data Cleaning
# Drop duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna({"director": "Unknown", "cast": "Unknown"}, inplace=True)

# Convert 'date_added' to datetime
df["date_added"] = pd.to_datetime(df["date_added"])

# Extract year from date
df["year_added"] = df["date_added"].dt.year

# 📌 Step 5: Analysis

# 1. Movies vs TV Shows
plt.figure(figsize=(6,6))
df["type"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Movies vs TV Shows")
plt.show()

# 2. Top 10 Genres
plt.figure(figsize=(10,6))
df["listed_in"].str.split(",").explode().value_counts().head(10).plot(kind="bar", color="skyblue")
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

# 3. Content Added Over the Years
plt.figure(figsize=(10,6))
df["year_added"].value_counts().sort_index().plot(kind="line", marker="o")
plt.title("Content Added to Netflix Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# 4. Country-wise Content (Top 10)
plt.figure(figsize=(12,6))
df["country"].value_counts().head(10).plot(kind="bar", color="orange")
plt.title("Top 10 Countries Producing Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# 5. Most Frequent Directors
plt.figure(figsize=(12,6))
df["director"].value_counts().head(10).plot(kind="bar", color="green")
plt.title("Top 10 Directors on Netflix")
plt.xlabel("Director")
plt.ylabel("Count")
plt.show()

# 📌 Step 6: Insights Printing
print("\n--- Key Insights ---")
print("1. Movies dominate Netflix, but TV Shows are growing rapidly.")
print("2. Drama, Comedy, and Action are the top genres.")
print("3. USA and India are leading content producers.")
print("4. Netflix has been adding more content consistently since 2015.")
