SHELL:=/bin/bash

build:
	docker build -t test_app .

init:
	docker run -d -p 80:8000 --name test_app_1 test_app
	docker exec -it test_app_1 python manage.py makemigrations app
	docker exec -it test_app_1 python manage.py migrate

bash-api:
	docker exec -it test_app_1 bash

stop:
	docker stop test_app_1

clear:
	docker stop test_app_1
	docker rm test_app_1
	docker rmi test_app
