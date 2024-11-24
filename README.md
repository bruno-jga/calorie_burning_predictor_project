# Calorie Burning Predictor

This is a simple web application that predicts the number of calories burned on gym exercise based on the user's age, weight, duration of exercise, heart rate, gender, etc. The application uses a machine learning model trained on a dataset of exercise data obtained from Kaggle (https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset).

The objective of this project was to learn how to use new tools like docker and learn how to create a web application using flask. 

This work is part of the Machine Learning Zoomcamp created by Alexey Grigorev.

## 1. Getting Started

I created a virtual environment to run the application.
To install the required packages, run the following command, on the same directory as the pipfile:

```pipenv install```

## 2. Explore the process of preprocessing the data and model testing

Check the notebook 'data_preparation_and_model_testing_ntbk.ipynb' .

## 3. Run the application

To run the application inside the docker container, first we need to build the image:

```docker build -t calorie_predictor .```

Then run the following command, to run the container:

```docker run -it --rm -p 9696:9696 calorie_predictor```

## 4. Test the application

The process of obtaining the prediction is simple and not fancy. I have a test_predict.py file that contains a URL (localhost) and "physical activity" dictionary that contains the values for the input variables. First we edit the variables then we run the program:

```python test_predict.py```	

And a prediction like this is returned:
{'Prediction of calories burned': 705.4508666992188}