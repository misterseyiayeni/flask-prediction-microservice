# Importing the necessary libraries
from flask import Flask, request
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
import json
import numpy as np

# Creating a Flask app
app = Flask(__name__)

# Creating a training dataset
X, y = make_blobs(n_samples=100000, centers=2, n_features=2, random_state=2)

# Fitting a logistic regression model on the training dataset
model = LogisticRegression()

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

# Defining a function that takes an input and returns a prediction
@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    n_samples = input_data['n_samples']
    X_new, y_new = make_blobs(n_samples=n_samples, centers=2, n_features=2, random_state=2)
    model.fit(X_new, y_new)
    prediction = model.predict(X_new)
    return json.dumps({'prediction': list(prediction)}, cls=NpEncoder)

# Running the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)