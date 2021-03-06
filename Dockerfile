FROM python:3.6-alpine

MAINTAINER Felix Breidenstein <mail@felixbreidenstein.de>
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache git openssh-client \
	&& pip install pipenv

RUN mkdir /code
WORKDIR /code

# Install dependencys
ADD Pipfile /code/
ADD Pipfile.lock /code/
RUN pipenv install

# Copy src
ADD . /code/
RUN rm -rf /code/database
VOLUME /code/database

CMD ["/code/entry.sh"]
