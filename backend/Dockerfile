FROM python:latest
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv gunicorn

COPY Pipfile Pipfile.lock /deploy/
WORKDIR /deploy

# Allows docker to cache installed dependencies between builds
RUN pipenv install --system --deploy --ignore-pipfile

# Adds our application code to the image
COPY . /deploy
EXPOSE 8000

CMD gunicorn --bind 0.0.0.0:8000 wsgi
