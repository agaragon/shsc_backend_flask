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

RUN useradd -ms /bin/bash myuser
USER myuser

ADD ./app /opt/app/
# run entrypoint.sh

ENTRYPOINT ["/opt/app/entrypoint.sh"]
