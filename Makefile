PHONY: reqs, dev

reqs:
	@pip freeze | tee requirements.txt

dev:
	@flask --app flaskr run --debug -p 8080
