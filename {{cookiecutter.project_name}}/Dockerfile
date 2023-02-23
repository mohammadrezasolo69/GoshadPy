# This docker file is used for production
# Creating image based on official python3 image
FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/{{cookiecutter.project_slug}}

# Installing all python dependencies
ADD requirements/ requirements/
RUN pip install -r requirements/requirements_production.txt



ADD * /app/{{cookiecutter.project_slug}}