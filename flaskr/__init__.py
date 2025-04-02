from flask import Flask, render_template, request
from flaskr.records import create_records


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def main():
        return render_template("base.html")

    @app.route("/records", methods=["GET", "POST"])
    def records_endpoint():
        if request.method == "POST":
            create_records(dict(request.form))

        return "OK"

    return app
