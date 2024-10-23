mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
celery:
	celery -A root worker -l INFO

flush:
	python3 manage.py flush
user:
	python3 manage.py createsuperuser --email admin@gmail.com

check:
	isort .
	flake8 .
loaddata:
	python3 manage.py loaddata country
data:
	python3 manage.py generate_data --user 5 --category 5
