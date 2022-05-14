FROM python:latest

RUN apt-get update

RUN mkdir /automation

COPY ./dummy_api /automation/dummy_api
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install

WORKDIR /automation/dummy_api