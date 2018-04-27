# enviroment
FROM python:3.6.4@sha256:bf0718e2882cabc144c9c07d758b09c65efc104a6ddc72a9a976f8b26f67c2ee
RUN apt-get update
RUN apt-get install -y postgresql-client

# Project Files and Settings
ARG SERVICE=horoscofox-service

ARG SERVICE_DIR=/app/${SERVICE}

ARG SERVICE_SRC=/app/${SERVICE}/src
ARG SERVICE_UTILS=/app/${SERVICE}/utils

RUN mkdir -p $SERVICE_DIR

WORKDIR $SERVICE_DIR

RUN pip install --upgrade pip

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install -U pipenv
RUN pipenv install --system  --deploy


COPY . $SERVICE_DIR

WORKDIR $SERVICE_SRC

RUN chmod -R 775 $SERVICE_UTILS/

