import flask
import time
from bars import BarScraper
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1> Popular Times Scraper</h1><p>This site is a prototype API for scraping popular times for bars and clubs.</p>"
    
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
    
@app.route('/api/v1/poptimes', methods=['GET'])
def api_id():
    query_parameters = request.args
    
    bar = query_parameters.get('bar')
    city = query_parameters.get('city')
    
    if not (bar and city):
        return page_not_found(404)
    else:
        PopTimesScraper = BarScraper(bar, city)
        times = PopTimesScraper.getPopTimes()
        
    #return jsonify(times)
    try:
        return jsonify(times[time.strftime('%H')])
    except:
        return jsonify(0)


if __name__=='__main__':
    app.run(debug=True)
