.PHONY: dev serve

dev:
	flask --app flaskr run --debug

serve:
	waitress-serve --call "flaskr:create_app"