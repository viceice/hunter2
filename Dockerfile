FROM python:3.6

RUN apt-get update && apt-get install -y \
    liblua5.2-dev \
    postgresql-client \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

VOLUME /storage

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
