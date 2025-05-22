from flask import Flask, render_template, request, make_response
from flaskr import database
import feedparser

def create_app():
    app = Flask(__name__)

    database.table_init_check() 

    @app.route("/")
    def home():
        feeds = database.load_saved_urls()
        return render_template('base.html', feeds=feeds)

    @app.route("/loadrss", methods=["POST"])
    def load_rss():
        print(request.form)
        return "OK", 200

    return app
