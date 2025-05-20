from flask import Flask, jsonify, request
from scraper import scrape_all
import os

app = Flask(__name__)

@app.route('/api/reva-about', methods=['GET'])
def get_about():
    # Scrape all URLs and return a summary of page titles and saved filenames
    summary = scrape_all()
    return jsonify(summary)

@app.route('/api/reva-search', methods=['GET'])
def search_reva():
    query = request.args.get('query', '').lower()
    summary = scrape_all()
    # Simple search: find titles containing the query
    results = {url: info for url, info in summary.items() if query in info['title'].lower()}
    return jsonify(results)

@app.route('/api/reva-search-content', methods=['GET'])
def search_reva_content():
    query = request.args.get('query', '').lower()
    summary = scrape_all()
    results = {}
    for url, info in summary.items():
        filename = info['filename']
        if filename and os.path.exists(filename):
            with open(filename, encoding='utf-8') as f:
                html = f.read().lower()
                if query in html or query in info['title'].lower():
                    results[url] = info
    return jsonify(results)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
