FROM python:3.6-alpine

RUN apk add --no-cache \
        lua5.2 \
	postgresql-client \
	postgresql-libs \
 && apk add --no-cache -t builddeps \
        gcc \
        git \
        lua5.2-dev \
	musl-dev \
	postgresql-dev

COPY requirements.txt /usr/src/app/
WORKDIR /usr
RUN pip install -r /usr/src/app/requirements.txt

RUN apk del --no-cache builddeps

WORKDIR /usr/src/app
COPY . .

RUN addgroup -g 500 -S django && adduser -s /sbin/nologin -G django -S -D -H -u 500 django
RUN install -d -g django -o django /config /static /uploads/events /uploads/puzzles
USER django

VOLUME ["/config", "/static", "/uploads/events", "/uploads/puzzles"]

EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
