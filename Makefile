all: venv install_req run

venv:
	python3 -m venv .venv

install_req:
	. .venv/bin/activate && pip install flask werkzeug

run:
	. .venv/bin/activate && python main.py

get_requirements:
	. .venv/bin/activate && pip freeze > requirements.txt

kill_port:
	npx kill-port 5000

clean:
	rm static/images/*.*

clean_all:
	rm -rf .venv
