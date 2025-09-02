# InvestHub (Desktop)

A Python Tkinter desktop app for stock market analysis with charts, comparisons, news, learning resources, notes, and notifications.

## Features
- Interactive charts from historical data (Yahoo Finance)
- Compare two stocks side-by-side
- Learning tab with curated videos
- Live market news (NewsAPI)
- Notes and notifications
- Simple registration/login backed by MySQL

## Project Structure
```
Investhub/
  HomePage.py        # Entry screen (Login / Register)
  LoginPage.py       # Login UI
  RegisterPage.py    # Registration UI (uses MySQL)
  Dashboard.py       # Main hub after login
  ChartPage.py       # Ticker chart visualizations (yfinance + matplotlib)
  ComparePage.py     # Compare two tickers
  AnalyzePage.py     # Simple ticker info view
  NewsPage.py        # Business headlines (NewsAPI)
  Notes.py, Notifications.py, Flashcard.py
  conn.py            # MySQL connection (edit credentials)
  assets (.png/.jpg), sample .pkl datasets, keras_model.h5
```

## Prerequisites
- Python 3.8+
- MySQL Server (local) or a MySQL-compatible instance
- A NewsAPI key (free) for headlines

## Setup
1) Create and activate a virtual environment (recommended)
```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

2) Install dependencies
```powershell
pip install -r requirements.txt
```

3) Configure database
- Create the database and table:
```sql
CREATE DATABASE sma;
USE sma;
CREATE TABLE userinfo(
  userid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  useremail VARCHAR(100) NOT NULL,
  usercontact BIGINT NOT NULL,
  userage INT NOT NULL,
  username VARCHAR(100) NOT NULL,
  userpassword VARCHAR(100) NOT NULL
);
```
- Update `Investhub/conn.py` if your MySQL credentials differ:
```
host="localhost", user="root", password="root123", database="sma"
```

4) NewsAPI key
- Open `Investhub/NewsPage.py` and replace the hardcoded API key with your own:
```
newsapi = NewsApiClient(api_key='<YOUR_KEY>')
```

## Run
From the project root or the `Investhub/` folder:
```powershell
cd Investhub
python HomePage.py
```

## Troubleshooting
- ModuleNotFoundError: install missing packages with `pip install <package>` or re-run `pip install -r requirements.txt`.
- MySQL connection error: ensure MySQL is running and credentials in `conn.py` are correct.
- News not loading: use a valid NewsAPI key.

## Publishing to GitHub
Initialize the repo and push (replace placeholders):
```powershell
cd C:\Users\Archit\Downloads\agri
git init
git add .
git commit -m "Initial commit: InvestHub desktop app"

git remote add origin https://github.com/<your-username>/<your-repo>.git
git branch -M main
git push -u origin main
```

## License
Specify your license of choice (e.g., MIT) in `LICENSE` if you plan to open-source.
