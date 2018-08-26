
from flask import Flask
import WebScrape

app = Flask(__name__)


@app.route("/")
def hello():
    return json.jsonify(f'{WebScrape.titles1}')
