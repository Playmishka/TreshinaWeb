all: venv install_req run

venv:
	python3 -m venv .venv

install_req:
	. .venv/bin/activate && pip install flask

clean_all:
	rm -rf .venv

kill_port:
	npx kill-port 5000

run:
	. .venv/bin/activate && python main.py