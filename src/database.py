import sqlite3
import pandas as pd
import os

def load_data():
    print("Loading data...")

    filename = "data/Tick Sightings.xlsx" # path to the excel dataset
    db_path = "data/ticks.db" # path to the sqlite database

    # check if the the file exists
    if not os.path.exists(filename):
        print(f"Could not find {filename} in this folder")
        return
    
    try:
        print("Reading Excel file...")
        df = pd.read_excel(filename) # read the excel file and save it into a pandas dataframe

        
        df = df.rename(columns = {
            "id": "id",
            "date": "date_time_reported",
            "location": "city",
            "latinName": "latin_name"
        })

        df["quantity"] = 1

        print("Connecting to database...")
        conn = sqlite3.connect(db_path)

        df.to_sql('sightings', conn, if_exists='replace', index=False)
        conn.close()
        print("Data loaded successfully into the database.")

    except Exception as e:
        print(f"Error connecting to database: {e}")
        return

        
if __name__ == "__main__":
    load_data()