FROM python:3.8.1-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \

  # Decrease image size by remove cachepip
  && rm -rf /var/cache/apk/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r requirements/base.txt

COPY ./compose/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

# Fix a case when container creates directories
# as root and host can't acces them.
ARG USER_ID
ARG USER_GROUP
RUN addgroup -g $USER_ID app && \
    adduser -D -u $USER_GROUP -G app app

USER app

WORKDIR /app

ENTRYPOINT ["/start"]
