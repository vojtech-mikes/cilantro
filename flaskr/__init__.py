from flask import Flask, render_template, request, Response
from flaskr.records import create_records, get_records, delete_records
from flaskr.contents import parse_contents


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def main():
        return render_template("base.html")

    @app.route("/records", methods=["GET", "POST", "DELETE"])
    def records_endpoint():
        if request.method == "POST":
            create_records(dict(request.form))
            records = get_records()
            return render_template("sources.html", sources=records)
        elif request.method == "GET":
            records = get_records()
            return render_template("sources.html", sources=records)
        elif request.method == "DELETE":
            source_to_del = request.args.get("source")
            delete_records(source_to_del)
            return Response(status=200)

    @app.route("/contents", methods=["GET"])
    def contents_endpoints():
        source_to_load = request.args.get("source")
        parse_contents(source_to_load)
        return "Hello, content"

    return app
