FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /bm8_api
WORKDIR /bm8_api
ADD . /bm8_api/
RUN pip install -r requirements.txt
