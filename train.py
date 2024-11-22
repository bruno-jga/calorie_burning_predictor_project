import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
import pickle

output_file = f'xgboost_final_model.bin'

df = pd.read_csv('gym_members_exercise_tracking.csv')
df.columns = df.columns.str.lower().str.replace(' ', '_')

categoricals = list(df.dtypes[df.dtypes == 'object'].index)

for col in categoricals:
    df[col]=df[col].str.lower().str.replace(' ', '_')

numericals = list(df.dtypes[df.dtypes != 'object'].index)

numericals = [
    'avg_bpm',
    'resting_bpm',
    'session_duration_(hours)',
    'calories_burned',
    'fat_percentage',
    'water_intake_(liters)',
    'workout_frequency_(days/week)',
    'experience_level',
    'bmi'
    ]

categoricals=['gender']

df_full_train, df_test = train_test_split(df[numericals+categoricals], test_size=0.2, random_state=39)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=39)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.calories_burned.values
y_val = df_val.calories_burned.values
y_test = df_test.calories_burned.values

del df_train['calories_burned']
del df_val['calories_burned']
del df_test['calories_burned']

def predict(df_val, dv, model):
    val_dicts = df_val.to_dict(orient='records')
    X_val = dv.transform(val_dicts)
    y_pred = model.predict(X_val)

    return y_pred

## Train with full data

y_full_train = (df_full_train.calories_burned)
del df_full_train['calories_burned']

full_train_dicts = df_full_train.to_dict(orient='records')
dv = DictVectorizer(sparse=True)
X_full_train = dv.fit_transform(full_train_dicts)

final_model = xgb.XGBRegressor(n_estimators=75,max_depth=3,eta=0.1)
final_model.fit(X_full_train, y_full_train)

with open(output_file,'wb') as f_out:
    pickle.dump((dv,final_model),f_out)


