# StreamWatch - OTT Data Cleaning Pipeline
# Tools: Python, Pandas, MySQL

import pandas as pd
import mysql.connector

# Load raw OTT data
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

# Clean and preprocess
def clean_data(df):
    df.dropna(subset=['title', 'type', 'release_year'], inplace=True)
    df['release_year'] = df['release_year'].astype(int)
    df['genre'] = df['genre'].fillna('Unknown')
    df['imdb_score'] = pd.to_numeric(df['imdb_score'], errors='coerce')
    return df

# Export to MySQL
def export_to_mysql(df, table_name):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="streamwatch_db"
    )
    cursor = conn.cursor()
    print(f"Exporting {len(df)} records to MySQL table: {table_name}")
    conn.close()

if __name__ == "__main__":
    netflix_df = load_data("data/netflix_titles.csv")
    netflix_df = clean_data(netflix_df)
    export_to_mysql(netflix_df, "netflix_titles")
    print("✅ Data pipeline complete.")
