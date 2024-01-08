FROM python:3.9.13

COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

RUN mkdir service
WORKDIR /service
ADD . /service

EXPOSE 8000
