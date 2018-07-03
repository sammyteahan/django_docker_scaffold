FROM python:3.4
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV development_docker
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r misc/requirements.txt
