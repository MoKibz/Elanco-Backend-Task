import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

app.title = "Elanco Placement Program: Technical Task - Backend"

class Analytics:
    def __init__(self):
        self.conn = get_db_connection()

    def get_regional_sightings(self):
        
        query = "SELECT city, SUM(Quantity) as total_quantity " \
        "FROM sightings " \
        "GROUP BY city " \
        "ORDER BY total_quantity DESC"

        results = self.conn.execute(query).fetchall()
        return results
    
    def get_species_sightings(self):

        query = "SELECT latin_name, SUM(Quantity) as total_quantity " \
        "FROM sightings " \
        "GROUP BY latin_name " \
        "ORDER BY total_quantity DESC"

        results = self.conn.execute(query).fetchall()
        return results
    
    def get_monthly_sightings(self):

        query = "SELECT strftime('%Y-%m', date_time_reported) as month, SUM(Quantity) as total_quantity " \
        "FROM sightings " \
        "WHERE date_time_reported IS NOT NULL " \
        "GROUP BY month " \
        "ORDER BY month ASC"

        results = self.conn.execute(query).fetchall()
        return results
    
    def get_weekly_sightings(self):

        query = "SELECT strftime('%Y-%W', date_time_reported) as week, SUM(Quantity) as total_quantity " \
        "FROM sightings " \
        "WHERE date_time_reported IS NOT NULL " \
        "GROUP BY week " \
        "ORDER BY week ASC"

        results = self.conn.execute(query).fetchall()
        return results
    
    def close_connection(self):
        self.conn.close()

def get_db_connection():
    conn = sqlite3.connect("data/ticks.db")
    conn.row_factory = sqlite3.Row
    return conn

class Sighting(BaseModel):
    id: str
    date_time_reported: str
    city: str
    species: str
    latin_name: str
    quantity: int

@app.get("/sightings", response_model=List[Sighting])
def get_sightings(city: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
    conn = get_db_connection()

    query = "SELECT * FROM sightings"
    parameters = []
    conditions = []

    if city:
        query += " WHERE city = ?"
        parameters.append(city)

    if start_date:
        conditions.append("date_time_reported >= ?")
        parameters.append(start_date)
    
    if end_date:
        conditions.append("date_time_reported <= ?")
        parameters.append(end_date)
    
    if conditions:
        if "WHERE" in query:
            query += " AND " + " AND ".join(conditions)
        else:
            query += " WHERE " + " AND ".join(conditions)
    
    query += " ORDER BY date_time_reported DESC"
    
    results = conn.execute(query, parameters).fetchall()
    conn.close()

    return [dict(row) for row in results]
    
@app.get("/analytics/regional/")
def regional_sightings():
    analytics = Analytics()
    results = analytics.get_regional_sightings()
    analytics.close_connection()
    return [dict(row) for row in results]

@app.get("/analytics/species/")
def species_sightings():
    analytics = Analytics()
    results = analytics.get_species_sightings()
    analytics.close_connection()
    return [dict(row) for row in results]

@app.get("/analytics/monthly/")
def monthly_sightings():
    analytics = Analytics()
    results = analytics.get_monthly_sightings()
    analytics.close_connection()
    return [dict(row) for row in results]

@app.get("/analytics/weekly/")
def weekly_sightings():
    analytics = Analytics()
    results = analytics.get_weekly_sightings()
    analytics.close_connection()
    return [dict(row) for row in results]



