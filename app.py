from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Home page with company logos
    return render_template('index.html')

@app.route('/years/<ticker>')
def years(ticker):
    # Load data to find available years
    filepath = f'summaries_{ticker.lower()}.json'
    with open(filepath, 'r') as file:
        data = json.load(file)
    years = list(data.keys())
    return render_template('years.html', ticker=ticker.upper(), years=years)

@app.route('/summary/<ticker>/<year>')
def summary(ticker, year):
    # Load summary data for the specific year
    filepath = f'summaries_{ticker.lower()}.json'
    with open(filepath, 'r') as file:
        data = json.load(file)
    content = data.get(year, {})
    return render_template('summary.html', ticker=ticker.upper(), year=year, content=content)

if __name__ == "__main__":
    app.run(debug=True)
