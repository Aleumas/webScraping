
from flask import Flask
from flask import jsonify
import WebScrape

app = Flask(__name__)


@app.route("/")
def hello():
    return (WebScrape.NewTitles)
