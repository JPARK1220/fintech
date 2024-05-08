from flask import Flask, render_template, jsonify, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summaries/<ticker>')
def summaries(ticker):
    try:
        with open(f'summaries_{ticker.lower()}.json', 'r') as f:
            data = json.load(f)
        return render_template('summary.html', data=data, ticker=ticker.upper())
    except FileNotFoundError:
        return jsonify({"error": "Data not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
