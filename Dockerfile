FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE keeper.settings.production

COPY ./requirements.txt /requirements.txt

# Install postgres client
RUN apk add --update --no-cache postgresql-client \
    && apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && pip install -r /requirements.txt \
    && apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN python manage.py collectstatic --no-input \
    && adduser -D keeper \
    && chown -R keeper /app/static
USER keeper