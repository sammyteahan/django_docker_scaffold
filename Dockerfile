FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV development_docker
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r misc/requirements.txt
RUN pip install pylint
