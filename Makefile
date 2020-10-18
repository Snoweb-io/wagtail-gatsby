start:
	python manage.py runserver localhost:4243

shell:
	python manage.py shell

mm:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

run:
	rm -rf ./.cache && rm -rf ./public && gatsby develop
