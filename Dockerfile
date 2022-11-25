FROM python:3.11-slim

WORKDIR /workspace

COPY ./requirements.txt requirements.txt

RUN pip install -U pip && \
    pip install -r requirements.txt