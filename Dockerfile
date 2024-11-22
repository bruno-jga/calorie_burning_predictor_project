FROM python:3.10.11-slim 

RUN pip install pipenv 

WORKDIR /calorie_burning_predictor
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy



