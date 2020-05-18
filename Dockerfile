FROM library/python:3.8-alpine

ADD . /src
WORKDIR /src

RUN python setup.py develop