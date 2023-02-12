FROM python:3.10.6-slim-buster

RUN mkdir /moresand
WORKDIR /moresand

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./dependencies.txt /moresand/dependencies.txt
RUN pip install -r dependencies.txt

COPY . /moresand