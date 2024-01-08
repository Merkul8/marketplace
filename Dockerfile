FROM python:3.9.13

COPY requirements.txt /temp/requirements.txt
RUN mkdir library
WORKDIR /library
ADD . /library

EXPOSE 8000

RUN apt-get update && apt-get install -y postgresql-client build-essential postgresql-server-dev-all

RUN pip install -r /temp/requirements.txt