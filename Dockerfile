FROM python:3.5-onbuild

ADD . /usr/src/docker/test_app/cat-dog
WORKDIR /usr/src/docker/test_app/cat-dog
CMD python manage.py runserver 0.0.0.0:8000
