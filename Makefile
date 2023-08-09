run:
	uvicorn main:app --reload

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt
