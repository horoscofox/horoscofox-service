FROM python:3.6.4@sha256:bf0718e2882cabc144c9c07d758b09c65efc104a6ddc72a9a976f8b26f67c2ee

# Project Files and Settings
ARG PROJECT=horoscofox
ARG PROJECT_DIR=/app/${PROJECT}

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install -U pipenv
RUN pipenv install --system --deploy


COPY . $PROJECT_DIR

 