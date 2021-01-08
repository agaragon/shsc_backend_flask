# pull official base image
FROM python

# set work directory
# WORKDIR /usr/src/app
WORKDIR /opt/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
ADD ./requirements.txt /tmp/requirements.txt
# COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /tmp/requirements.txt

# copy project
# COPY . /opt/app
ADD ./app /opt/app/
# run entrypoint.sh
ENTRYPOINT ["/opt/app/entrypoint.sh"]


# FROM alpine:latest
# RUN apk add --no-cache --update python3 py3-pip bash postgresql-dev python3-dev musl-dev gcc
# ENV DATABASE_URL $DATABASE_URL
# ADD ./requirements.txt /tmp/requirements.txt
# RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt
# ADD ./app /opt/app/
# # RUN adduser -D myuser
# WORKDIR /opt/app
# # USER myuser
# # CMD gunicorn --bind 0.0.0.0:5000 wsgi 
# ENTRYPOINT ["/opt/app/entrypoint.sh"]
