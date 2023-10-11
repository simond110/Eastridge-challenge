# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1
ENV REDIS_HOSTNAME redis

RUN apk add --no-cache gcc musl-dev python3-dev

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev

RUN pip install --upgrade pip

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt


RUN apk del .tmp
# copy project
COPY . .

# add and run as non-root user
RUN adduser -D myuser
USER myuser
