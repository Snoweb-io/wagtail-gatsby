start:
	python manage.py runserver localhost:4243

shell:
	python manage.py shell

mm:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

develop:
	npm run build-plugin && gatsby clean && gatsby develop

worker:
	celery multi stopwait cms_worker --pidfile="./celery/%n.pid" --logfile="./celery/%n%I.log"
	celery multi start cms_worker -A cms --pidfile="./celery/%n.pid" --logfile="./celery/%n%I.log"

worker_dev:
	yes | celery -A cms purge && celery -A cms worker -l info

deploy:
	gatsby build && npm run deploy && aws cloudfront create-invalidation --distribution-id $AWS_DISTRIBUTION_ID --paths "/*"
