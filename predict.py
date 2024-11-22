import pickle
from flask import Flask, request,jsonify

model_file="xgboost_final_model.bin"

with open(model_file,'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('Calorie Prediction')

@app.route('/predict', methods=['POST'])
def predict():
    physical_activity=request.get_json()

    X=dv.transform([physical_activity])
    y_pred=model.predict(X)

    result = {
        'Prediction of calories burned': float(y_pred)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=9696)