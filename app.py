from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    # home page with company logos
    return render_template('index.html')

@app.route('/years/<ticker>')
def years(ticker):
    # load data to find available years
    filepath = f'summaries_{ticker.lower()}.json'
    with open(filepath, 'r') as file:
        data = json.load(file)
    years = list(data.keys())
    return render_template('years.html', ticker=ticker.upper(), years=years)

@app.route('/insights/<ticker>/<year>')
def insights(ticker, year):
    # load summary data for the specific year
    filepath = f'summaries_{ticker.lower()}.json'
    with open(filepath, 'r') as file:
        data = json.load(file)
    content = data.get(year, {})
    return render_template('insights.html', ticker=ticker.upper(), year=year, content=content)

@app.route('/references')
def references():
    # You can include more links or modify this list according to your needs
    links = [
        {"url": "https://www.sec.gov/edgar/searchedgar/companysearch.html", "description": "SEC EDGAR Search"},
        {"url": "https://www.openai.com/", "description": "OpenAI Homepage"},
        {"url": "https://www.apple.com/", "description": "Apple"},
        {"url": "https://www.microsoft.com/", "description": "Microsoft"}
    ]
    return render_template('references.html', links=links)


if __name__ == "__main__":
    app.run(debug=True)
