all: venv install_req run

venv:
	python3 -m venv .venv

install_req:
	pip install flask werkzeug

run:
	python main.py

get_requirements:
	pip freeze > requirements.txt

kill_port:
	npx kill-port 5000

clean:
	rm static/images/*.*

clean_all:
	rm -rf .venv
