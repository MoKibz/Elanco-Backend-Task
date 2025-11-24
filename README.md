# Elanco Tick Tracker Backend

A backend API MVP for tracking tick sightings across the UK, built for the Elanco Placement Program technical backend task.

## Getting Started

### Prerequisites

* Python 3.10 or higher

* Virtual environment (recommended)

### Installation
**1. Clone the repository (using Terminal/Command Prompt/PowerShell)**
```
git clone https://github.com/MoKibz/Elanco-Backend-Task.git

cd "Elanco-Backend-Task"

```

**2. Set up the environment**
```
python -m venv .venv

# Windows:
.venv\Scripts\Activate

# Mac/Linux:
source .venv/bin/activate

```

**3. Install dependencies**
```
pip install "fastapi[standard]" pandas openpyxl

```
### Running the Project

**1. Load the Data (run this script once to read the Excel file and populate the SQLite database)**
```
python src/database.py

```

*You should see a "Data loaded successfully into the database" message.*

**2. Start the Server**
```
fastapi dev src/main.py

```
**3. View the API**

Open your browser by going to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 


## Project Walkthrough:

Click [here](https://youtu.be/gS-a7ozUhME) to access the video walkthrough

---

# Documentation and thought process

This project is built as a Minimum Viable Product (MVP) backend.

## 1. Choice of tools
* **FastAPI:** It is incredibly fast to work with and is a modern solution. Automatically checks if the data is correct (through the use of Pydantic) and generates its own documentation page, which saved me time to build the project.
* **SQLite:** Considering the size of the dataset (around 1000 entries) there was not a need of a massive database server. SQLite is a simple file-based database which can be run instantly without a complex setup.
* **Pandas:** The dataset is easier to read from '.xlsx' file using Pandas built-in functions which cleans up column names and converts to SQLite database.
## 2. Data handling
The data loading is separate from the main app server to keep the code clean and maintainable.
* **Safe Loading:** The script (`src/database.py`) wipes the slate clean and reloads the data fresh every time it is run. This prevents any duplicates in the data.
* **Clean Names:** The raw excel dataset had mixed naming sytles which have been renamed using the standard Python style at the start to ensure consistency and readability of the code throughout.
## 3. How the Code is Structured
Used a Service Layer pattern (the `Analytics` class) to organize the logic.
* **Why:** To prevent complex SQL queries cluttering up the API routes.
* **The Benefit:** Makes the code modular, if switching databases, therefore only requiring updating the `Analytics` class.
## 4. If I had more time...
* **Upgrade the Database:** Move from SQLite to PostgreSQL to handle more users at once.
* **Automate Updates:** Instead of running the script manually, I would set up a background task to check for new data automatically at set time intervals.
