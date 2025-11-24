# Elanco Tick Tracker Backend

A backend API MVP for tracking tick sightings across the UK, built for the Elanco Placement Program technical task.

## Getting Started

### Prerequisites

* Python 3.10 or higher

* Virtual environment (recommended)

### Installation
1. Clone the repository (or navigate to the project folder)
```
cd "Elanco Backend Task"

```

2. Set up the environment
```
python -m venv .venv

# Windows:
.venv\Scripts\Activate

# Mac/Linux:
source .venv/bin/activate

```

3. Install dependencies
```
pip install "fastapi[standard]" pandas openpyxl

```
### Running the Project

1. Load the Data. Run this script once to read the Excel file and populate the SQLite database.
```
python src/database.py

```

*You should see a "Data loaded successfully into the database" message.*

2. Start the Server
```
fastapi dev src/main.py

```
3. View the API
Open your browser by clicking [here](https://www.google.com/search?q=http://127.0.0.1:8000/docs)


## Project Walkthrough:

Click [here]() to access the video walkthrough
