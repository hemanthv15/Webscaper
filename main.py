import flask
from scraper import scrape_reviews

app = flask.Flask(__name__)

@app.route('/api/reviews', methods=['GET'])
def index():
    url = flask.request.args.get('page')
    if not url:
        return flask.jsonify({'error': 'Page URL is required'}), 400
    
    try:
        reviews = scrape_reviews(url)
        return flask.jsonify(reviews)
    except Exception as e:
        return flask.jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)