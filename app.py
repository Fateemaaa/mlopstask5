from flask import Flask, request, jsonify
import joblib
import pandas as pd


from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
#from sklearn.preprocessing import power_transform



# Load the pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.json

    # Preprocess the data if needed
    # Example: Convert JSON data to pandas DataFrame
    df = pd.DataFrame(data)
    print(df)

    # Make predictions using the loaded model
    predictions = model.predict(df)


    # Return the predictions as JSON response
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
