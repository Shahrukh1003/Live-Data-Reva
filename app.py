from flask import Flask, jsonify
from scraper import scrape_all

app = Flask(__name__)

@app.route('/api/reva-about', methods=['GET'])
def get_about():
    # Scrape all URLs and return a summary of page titles and saved filenames
    summary = scrape_all()
    return jsonify(summary)

