FROM python:latest
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac \
    ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig zlib1g-dev libpulse-dev tesseract-ocr-pol

RUN pip install pipenv gunicorn textract

COPY Pipfile Pipfile.lock /deploy/
WORKDIR /deploy

# Allows docker to cache installed dependencies between builds
RUN pipenv install --system --deploy --ignore-pipfile

# Adds our application code to the image
COPY . /deploy
EXPOSE 8000

CMD gunicorn --bind 0.0.0.0:8000 wsgi
