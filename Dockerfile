FROM python:3.10.11-slim 

RUN pip install pipenv 

WORKDIR /calorie_burning_predictor
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "xgboost_final_model.bin",  "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "predict:app"]



