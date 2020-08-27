
#Simple file for Django
FROM python:3

# Ensures all stdout gets to console and not stuck in a buffer
ENV PYTHONUNBUFFERED 1
# /code is where all the source will reside, will be mapped volume
WORKDIR /code
# copy the requirements generated from venv
COPY requirements.txt /code/
# install all those dependencies
RUN pip install -r requirements.txt
# copy all the files from mysite
COPY . /code/
