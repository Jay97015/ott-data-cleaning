import pandas as pd
import numpy as np

print("--- PHASE 1: LOADING THE MESSY DATA ---")
# 1. Our simulated messy streaming dataset
raw_data = {
    'Title': ['Stranger Things', 'Wednesday', 'The Irishman', 'Stranger Things', 'Squid Game'],
    'Category': ['TV Show', 'tv show', 'Movie', 'TV Show', 'Movie'],
    'Duration': ['4 Seasons', '1 Season', '209 min', '4 Seasons', np.nan],
    'Release_Date': ['July 15, 2016', 'November 23, 2022', 'November 27, 2019', 'July 15, 2016', 'September 17, 2021'],
    'Director': [np.nan, 'Tim Burton', 'Martin Scorsese', np.nan, 'Hwang Dong-hyuk']
}

df = pd.DataFrame(raw_data)
print(df)
print("\n" + "="*50 + "\n")

print("--- PHASE 2: CLEANING THE DATA ---")

# Step A: Drop exact duplicates (Removes the extra 'Stranger Things' row)
df_clean = df.drop_duplicates()
print("1. Duplicates removed.")

# Step B: Standardize text casing (Fixes 'tv show' to 'TV Show')
df_clean['Category'] = df_clean['Category'].str.title()
print("2. Text casing standardized.")

# Step C: Handle missing values in 'Director' safely
df_clean['Director'] = df_clean['Director'].fillna('Unknown Director')
print("3. Missing directors handled safely.")

# Step D: Standardize Date formats to YYYY-MM-DD
df_clean['Release_Date'] = pd.to_datetime(df_clean['Release_Date'].str.strip())
print("4. Dates converted to standard datetime format.")

# Step E: Fill missing duration gaps
df_clean['Duration'] = df_clean['Duration'].fillna('Data Missing')
print("5. Missing durations addressed.\n")

print("--- PHASE 3: FINAL CLEANED DATASET ---")
print(df_clean)
